install:
	pip install -r requirements.txt
 
uninstall:
	pip uninstall driver

make_env:
	python3 -m venv env
	source env/bin/activate


clean:
	find . -type f -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -rf {} +
	find . -type f -name "*.pyo" -exec rm -rf {} +


.PHONY: clean
