testenv:
	pip install -e .
	pip install -r requirements-dev.txt

release:
	python setup.py sdist upload -r pypi

# Test it via `pip install -i https://testpypi.python.org/pypi <project_name>`
test-release:
	python setup.py sdist upload -r test

clean:
	rm -rf dist/
	rm MANIFEST
	find . -name "*.pyc" -exec rm {} \;
