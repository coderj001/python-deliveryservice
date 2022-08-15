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

## Backgound of the application

Kiki, a first-time entrepreneur from the city of Koriko has decided to open a small distance courier service to deliver packages, with her friend Tombo and cat Joji.

Kiki has invested in N no. of vehicles and have driver partners to drive each vehicle & deliver packages.

## Problem 1

Delivery Cost Estimation with Offers

Since it’s a new business, the team has decided to pass coupons
around the town which will help them attract more customers.

Discounts Section
<table style="border:0.5px solid gray">
<th>
<td>Distance (km)</td>
<td>Weight (kg)</td>
</th>
<tr>
<td>
OFR001
10% Discount
</td>
<td>< 200</td>
<td>70-200</td>
</tr>

<tr>
<td>
OFR002
7% Discount
</td>
<td>50-150</td>
<td>100-250</td>
</tr>

<tr>
<td>
OFR003
5% Discount
</td>
<td>50-250</td>
<td>10-150</td>
</tr>


</table>

<br>

### Calculate Delivery cost

<code>
Delivery Cost = Base Delivery Cost + (Package Total Weight * 10) +
(Distance to Destination * 5) - Discount Price
</code>

### How to execute Problem 1

Since this application uses makefile, Build & run the application using the following command

```sh
$ make
$ make run1
```

Add the enter the input parameters as below in 

```sh
base_delivery_cost no_of_packges
pkg_id pkg_weight_in_kg distance_in_km offer_code
....
```

For example,
```sh
100 3
PKG1 5 5 OFR001
PKG2 15 5 OFR002
PKG3 10 100 OFR003
```

It gives output as the below format
```sh
pkg_id discount1 total_cost
...
```


## Problem 2

Delivery Time Estimation
Now all these packages should be delivered to their destinations in
the fleet of vehicles Kiki owns. She has N no. of vehicles available for
delivering the packages.

To note: 
<code>
1. Each Vehicle has a on limit (L) maximum weight (kg) that it can carry.
2. All Vehicles travel at the same and in the It is assumed that all the destinations can be covered in a single route.
3. Shipment should contain max packages vehicle can carry in a trip.
4. Should prefer heavier packages when there are multiple shipments with the same no. of packages.
5. If the weights are also the same, preference should be given to the shipment which can be delivered first.
</code>


### How to execute Problem 2

Build & run the application using the following command

```sh
$ make
$ make run2
```

Add the enter the input parameters as below in 

```sh
base_delivery_cost no_of_packges
pkg_id pkg_weight_in_kg distance_in_km offer_code
....

no_of_vehicles max_speed max_carriable_weight
```

For example,
```sh
100 5
PKG1 50 30 OFR001
PKG2 75 125 OFFR0008
PKG3 175 100 OFFR003
PKG4 110 60 OFFR002
PKG5 155 95 NA
2 70 200
```

It gives output as the below format
```sh
pkg_id discount total_cost estimated_delivery_time_in_hours
...
```


#### Test
Run All testcase by `make test`

### Future Updates
1. Added sqlalchemy to have db connect
2. Build rest api around it
