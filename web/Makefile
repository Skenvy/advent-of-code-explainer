# Inherit the venv setup utilities. This is otherwise
# an altered version of this file generate by pelican
include ../Makefile

PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

# Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html
DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

# Set the RELATIVE variable to 1 to enable relative urls
# RELATIVE ?= 0
# ifeq ($(RELATIVE), 1)
# 	PELICANOPTS += --relative-urls
# endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif

# remove the generated files
.PHONY: clean_this
clean_this: clean
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

# (re)generate the web site
.PHONY: generate
generate: clean_this
	$(VE) "$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

# serve site at http://localhost:8000 | make serve [PORT=8000]
.PHONY: serve
serve: generate
	$(VE) "$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

# generate using production settingss
.PHONY: publish
publish: clean_this
	$(VE) "$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
