.PHONY: help extract install-scripts

VENV := scripts/.venv
PYTHON := $(VENV)/bin/python3

help:
	@echo "Cibles disponibles :"
	@echo "  make install-scripts              — crée le venv et installe les dépendances Python"
	@echo "  make extract FILE=<fichier.pptx>  — extrait le contenu d'un PPTX"
	@echo "  make extract FILE=<fichier.pptx> OUT=<dossier>"

$(VENV):
	python3 -m venv $(VENV)

install-scripts: $(VENV)
	$(PYTHON) -m ensurepip --upgrade
	$(PYTHON) -m pip install -r scripts/requirements.txt

## Extraction PPTX
## Usage : make extract FILE=mon_cours.pptx
##         make extract FILE=mon_cours.pptx OUT=src/content/courses ASSETS_OUT=public/assets
OUT ?= src/content/courses
ASSETS_OUT ?= public/assets
extract: $(VENV)
ifndef FILE
	$(error FILE est requis. Exemple : make extract FILE=mon_cours.pptx)
endif
	$(PYTHON) scripts/pptx_extract.py $(FILE) $(OUT) $(ASSETS_OUT)
