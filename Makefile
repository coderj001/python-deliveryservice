.DEFAULT_GOAL := build

APPLICATION=python-deliveryservice
BIN=venv/bin/

venv:
	virtualenv venv


build:
	$(BIN)pip install -e .
	$(BIN)python setup.py build

test:
	$(BIN)python -m pytest .

run1:
	$(BIN)python -m pytest tests/cli_test.py::test_cost

run2:
	$(BIN)python -m pytest tests/cli_test.py::test_time

# Docker
docker_build:
	docker build -t cli .

docker_test:
	docker run --rm -it --entrypoint "" cli python -m pytest .


docker_run1:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_cost

docker_run2:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_time
