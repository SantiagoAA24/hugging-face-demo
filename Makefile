install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=geeting \
		--cov=smath  --cov=web tests
	python -m pytest -nbval notebook.ipynb

debug:
	python -m pytest -vv --pdb

one-test:
	python -m pytest -vv tests/test_greeting.py::test_my_name_4

debugthree:
	python -m pytest -vv --pdb --maxfail=4

format:
	black *.py

lint:
	pylint disable=R,C *-py

all: install lint test format