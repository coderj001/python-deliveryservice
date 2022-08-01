### python-deliveryservice
> python, typer, docker

#### Setup
1. Please download repo `git clone https://github.com/coderj001/python-deliveryservice.git` and `cd python-deliveryservice`
##### For simple python install
2. Run `make venv` to have virtualenv, `make build`
3. Now run `python cli.py --help`
##### For Docker
2. Run `docker_build` to install and build docker image
3. Now run `docker run --rm -it cli --help`

Application have appropriate guide use `--help` to get more info.<br />
**Why use docker?**
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

#### Application Background
Kiki, a first-time entrepreneur from the city of
Koriko has decided to open a small distance
courier service to deliver packages, with her
friend Tombo and cat Joji.
Kiki has invested in N no. of vehicles and
have driver partners to drive each vehicle& deliver packages.

##### Problem 01
**Delivery Cost Estimation with Offers**
<br />
Since it’s a new business, the team has decided to pass coupons
around the town which will help them attract more customers.
Coupons,<br />
  coupon              | distance(km) | weight(kg)<br />
  OFR001 10% Discount	|  <200        | 70-200    <br />
  OFR002 7% Discount	|  50-150      | 100-250   <br />
  OFR003 5% Discount	|  50-250      | 10-150    <br />

Delivery Cost = Base Delivery Cost + (Package Total Weight * 10) + (Distance to Destination * 5) - Discount Price

**Execute for  Problem 01:** <br />
Since application is build, run `make run1` or `make docker_run1` for docker
to run test case for problem 01.
Add the enter the input parameters as below in
```
base_delivery_cost no_of_packges
pkg_id pkg_weight_in_kg distance_in_km offer_code
....

```
For example,
```
100 3
PKG1 5 5 OFR001
PKG2 15 5 OFR002
PKG3 10 100 OFR003
```
It gives output as the below format
```
pkg_id discount1 total_cost
...
```
##### Problem 02
Delivery Time Estimation Now all these packages should be delivered to their destinations in the fleet of vehicles Kiki owns. She has N no. of vehicles available for delivering the packages. <br />

Mental Note:
```
1. Each Vehicle has a on limit (L) maximum weight (kg) that it can carry.
2. All Vehicles travel at the same and in the It is assumed that all the destinations can be covered in a single route.
3. Shipment should contain max packages vehicle can carry in a trip.
4. Should prefer heavier packages when there are multiple shipments with the same no. of packages.
5. If the weights are also the same, preference should be given to the shipment which can be delivered first.
```

**Execute for  Problem 02:** <br />
As application is build run `make run2` or `make docker_run2` <br />

Add the enter the input parameters as below in
```
base_delivery_cost no_of_packges
pkg_id pkg_weight_in_kg distance_in_km offer_code
....

no_of_vehicles max_speed max_carriable_weight
```

For Example,

```
100 5
PKG1 50 30 OFR001
PKG2 75 125 OFFR0008
PKG3 175 100 OFFR003
PKG4 110 60 OFFR002
PKG5 155 95 NA
2 70 200
```
Output format
```pkg_id discount total_cost estimated_delivery_time_in_hours
```

### Future Updates
1. Problem 2 need to me more config
2. Added sqlalchemy to keep track for data
3. Build rest api around it
