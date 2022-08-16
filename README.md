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

#### How to run
**For cost**
```
python cli.py cost --base-delivery-price base_delivery_cost --package-details "pkg_id1 pkg_weight1_in_kg distance1_in_km offer_code1" --package-details "pkg_id2 pkg_weight2_in_kg distance2_in_km offer_code2" ...
```
example,
```
python cli.py cost --base-delivery-price 100 --package-details "PKG1 5 5 OFR001" --package-details "PKG2 15 5 OFR002" --package-details "PKG3 10 100 OFR003"
```

**For time**
```
python cli.py time --base-delivery-price base_delivery_cost --package-details "pkg_id1 pkg_weight1_in_kg distance1_in_km offer_code1" ... --vehicle-details no_of_vehicles max_speed max_carriable_weight
```
example,
```
python cli.py time --base-delivery-price 100 --package-details "PKG1 50 30 OFR001" --package-details "PKG2 75 125 OFFR0008" --package-details "PKG3 175 100 OFFR003" --package-details "PKG4 110 60 OFFR002" --package-details "PKG5 155 95 NA" --vehicle-details 2 70 200
```


#### Test
Run All testcase by `make test`

### Future Updates
1. time est is not working properly need to config
2. Added sqlalchemy to have db connect
3. Build rest api around it
