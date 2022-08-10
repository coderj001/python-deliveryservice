### python-deliveryservice
> python, typer, docker

#### Setup
1. Please download repo `git clone https://github.com/coderj001/python-deliveryservice.git` and `cd python-deliveryservice`
##### For simple python install (Please make sure python >= 3.9 installed)
2. Run `make venv` to have virtualenv,Now run `make build`
3. Now run `python cli.py --help`
##### For Docker (Please make sure docker is installed)
2. Run `docker_build` to install and build docker image
3. Now run `docker run --rm -it cli --help`

Application have appropriate guide use `--help` to get more info.<br />
**Why use docker?**
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

#### Test
Run All testcase by `make test`

### Future Updates
1. Added sqlalchemy to have db connect
2. Build rest api around it
