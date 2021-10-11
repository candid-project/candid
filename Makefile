PWD = $(shell pwd)
VENV = $(PWD)/.venv
ENV_D = $(PWD)/env.d
BIN_FLAKE8 = $(VENV)/bin/flake8
BIN_ISORT = $(VENV)/bin/isort
BIN_PIP = $(VENV)/bin/pip
BIN_PYTHON = $(VENV)/bin/python
BIN_PYTEST = $(VENV)/bin/pytest
BIN_UVIVORN = $(VENV)/bin/uvicorn

PYTEST_ARGS ?=


# .DEFAULT_GOAL = null
# .PHONY = null
NPROC ?= $(shell nproc)



clean:
	rm -rf $(VENV)

flake8:
	$(BIN_FLAKE8)

isort:
	$(BIN_ISORT) **/*.py --filter-files --interactive

isort_check:
	$(BIN_ISORT) **/*.py --filter-files --check-only

start:
	$(BIN_UVIVORN) candid.main:app --reload

test_all:
	$(BIN_PYTEST) -n auto $(PYTEST_ARGS)
