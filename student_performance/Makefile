all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP=student_performance STUDENT_PERFORMANCE_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	STUDENT_PERFORMANCE_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist

data:
	venv/bin/python src/data/process_data.py data/raw/ data/processed/

fit:
	venv/bin/python src/model/model.py data/processed/chemistry.csv --test True
.PHONY: all clean data
