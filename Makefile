VENV=python3 -m venv .ve
VE=source .ve/bin/activate && 
PIP_VERSION=24.3.1
PIP_PIP=pip install --upgrade pip==$(PIP_VERSION)
PIP_REQ=pip install --upgrade -r
VENV_REQS=requirements-venv.txt
FROZEN_VENV_REQS=requirements-venv-frozen.txt
TEST=pytest
TOX=tox

LINT_FOLDERS=src tests .demo/_
PYLINT=pylint --recursive=y --disable=C,R,I --enable=F,E,W --output-format=colorized,text:pylint.log --msg-template='{C} {path}:{line}:{column}: {msg_id}: {msg} ({symbol})' $(LINT_FOLDERS)
FLAKE8=flake8 --color=always -vv --output-file=flake8.log $(LINT_FOLDERS)

PACKAGE_VERSION=$$(cut -d \" -f 2 src/advent_of_code_explainer/__version__.py)
SPHINX_BUILD_SOURCE=sphinx-apidoc -Me -V $(PACKAGE_VERSION) -R $(PACKAGE_VERSION) -f -o docs/source src/
VERIFY_BUILT_MSG=echo "Exit if a change to the built Sphinx rst's is not committed"
VERIFY_BUILT_ERR=git add docs && git diff --exit-code --cached --stat -- docs/
TWINE=twine upload --config-file ./.pypirc --repository

SHELL:=/bin/bash

# to setup from frozen reqs
.PHONY: setup
setup:
	$(VENV)
	$(VE) $(PIP_PIP)
	$(VE) $(PIP_REQ) $(FROZEN_VENV_REQS)

# to clean setup from loose reqs and refreeze
.PHONY: setup_refresh
setup_refresh:
	rm -rf .ve
	$(VENV)
	$(VE) $(PIP_PIP)
	$(VE) $(PIP_REQ) $(VENV_REQS)
	$(VE) pip freeze > $(FROZEN_VENV_REQS)
	sed -i '/^pkg_resources/d' $(FROZEN_VENV_REQS)
	sed -i '/^pkg-resources/d' $(FROZEN_VENV_REQS)

# full clean
.PHONY: clean clean_again
clean clean_again:
	rm -rf src/*.egg-info/
	rm -rf dist/
	rm -rf */__pycache__/
	rm -rf */*/__pycache__/
	rm -rf .pytest_cache/
	rm  -f pylint.log
	rm  -f flake8.log
	rm -rf docs/build/

# http://localhost:44449/
# http://localhost:44449/src.advent_of_code_explainer.html
.PHONY: pydoc_server
pydoc_server:
	$(VE) python -m pydoc -b

.PHONY: verify_built_checkin
verify_built_checkin: clean
	$(VE) $(SPHINX_BUILD_SOURCE)
	$(VERIFY_BUILT_MSG)
	$(VERIFY_BUILT_ERR)

# https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
# https://www.sphinx-doc.org/en/master/man/sphinx-build.html
.PHONY: docs
docs: clean
	$(VE) $(SPHINX_BUILD_SOURCE)
	$(VE) sphinx-build -a -b dirhtml -W --keep-going -n docs/source docs/build

# http://localhost:8000/docs/build/
# http://localhost:8000/docs/build/advent_of_code_explainer/
.PHONY: server
server:
	python3 -m http.server 8000

.PHONY: test
test:
	$(VE) $(TEST)

# Pytest with tox
.PHONY: tox
tox: clean
	$(VE) $(TOX)

# https://pylint.readthedocs.io/en/latest/user_guide/configuration/all-options.html
# https://pylint.readthedocs.io/en/latest/user_guide/messages/index.html
# https://flake8.pycqa.org/en/latest/user/configuration.html
# https://flake8.pycqa.org/en/latest/user/options.html#options-list
.PHONY: lint
lint: clean
	$(VE) $(PYLINT)
	$(VE) $(FLAKE8)

.PHONY: build
build: test lint verify_built_checkin clean_again
	$(VE) python -m build
	$(VE) pip install --force-reinstall dist/*-none-any.whl

# https://twine.readthedocs.io/en/stable/#twine-upload
.PHONY: upload_test
upload_test: build
	$(VE) $(TWINE) testpypi dist/*

.PHONY: upload
upload: upload_test
	$(VE) $(TWINE) pypi dist/*
