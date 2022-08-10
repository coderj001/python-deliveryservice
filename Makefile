.DEFAULT_GOAL := build

APPLICATION=python-deliveryservice

venv:
	virtualenv venv
	. $(dir $(realpath $(lastword $(MAKEFILE_LIST))))venv/bin/activate


build:
	./venv/bin/activate; pip install -e .
	./venv/bin/activate; python setup.py build

test:
	./venv/bin/activate; pytest .

run1:
	./venv/bin/activate; pytest tests/cli_test.py::test_cost

run2:
	./venv/bin/activate; pytest tests/cli_test.py::test_time

# Docker
docker_build:
	docker build -t cli .

docker_test:
	docker run --rm -it --entrypoint "" cli python -m pytest .


docker_run1:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_cost

docker_run2:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_time
