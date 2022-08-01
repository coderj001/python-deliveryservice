.DEFAULT_GOAL := build

APPLICATION=python-deliveryservice

venv:
	virtualenv venv
	source ./venv/bin/activate

build:
	pip install -e .
	python setup.py build

test:
	pytest .

run1:
	pytest tests/cli_test.py::test_cost

run2:
	pytest tests/cli_test.py::test_time

# Docker
docker_build:
	docker build -t cli .

docker_test:
	docker run --rm -it --entrypoint "" cli python -m pytest .


docker_run1:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_cost

docker_run2:
	docker run --rm -it --entrypoint "" cli python -m pytest tests/cli_test.py::test_time
