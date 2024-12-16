VE=source .ve/bin/activate && 
PKG_NAME=advent-of-code-explainer
.PHONY: install demo everything
SHELL:=/bin/bash

install:
	python3 -m venv .ve
	$(VE) pip install --upgrade pip
	$(VE) pip install --upgrade $(PKG_NAME)-*-none-any.whl

demo:
	$(VE) find ./_/*.py -maxdepth 1 -type f | xargs -L1 python

everything: install demo
