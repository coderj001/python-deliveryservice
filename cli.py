from typing import List, Tuple

import typer
from rich import print
from typer import Typer

from deliveryservice.delivery.cost_est import calculate_package_groups
from deliveryservice.delivery.discount import Discounts, mock_all_discounts
from deliveryservice.delivery.package import Package
from deliveryservice.delivery.packages import Packages
from deliveryservice.delivery.vehicle import Vehicles

app = typer.Typer()  # type: Typer

discounts = mock_all_discounts()


@app.command(name="cost", help="Find delivery cost for packages")
def find_delivery_cost_for_packages(
    base_delivery_price: int = typer.Option(default=None, help="Base delivery price"),
    package_details: List[str] = typer.Option(
        [],
        help="""Added details of package with space
             pkg_id pkg_weight_in_kg distance_in_km offer_code
        ex: PKG1 5 5 OFR001""",
    ),
):
    all_packages = Packages()
    for package_detail in package_details:
        list_values: List[str | int] = package_detail.split(" ")
        package_id, weight, distance, coupon = [
            str(list_values[0]),
            int(list_values[1]),
            int(list_values[2]),
            str(list_values[3]),
        ]
        _discounts = Discounts()
        _discounts.add_list_of_discount(discounts.get_discount_by_coupon([coupon]))
        pkg = Package(
            pkg_id=package_id,
            base_cost=base_delivery_price,
            distance=distance,
            weight=weight,
            discounts=_discounts,
        )
        all_packages.add_package(pkg)
    all_packages.calculate_delivery_cost()
    output: str = ""
    for pkg in all_packages.packages:
        output += "{} {} {}\n".format(pkg.pkg_id, pkg.discount_cost, pkg.total_cost)
    print(output)


@app.command(name="time", help="Calculate delivery time estimation")
def calculate_delivery_time_estimation(
    base_delivery_price: int = typer.Option(default=None, help="Base delivery price"),
    package_details: List[str] = typer.Option(
        [],
        help="Added details of package with space pkg_id pkg_weight_in_kg distance_in_km offer_code ex: PKG1 5 5 OFR001",
    ),
    vehicle_details: Tuple[int, int, int] = typer.Option(
        (None, None, None),
        help="Added vehicle details no_of_vehicles max_speed max_carriable_weight ex: 2 70 200",
    ),
):
    all_packages = Packages()
    for package_detail in package_details:
        list_values: List[str | int] = package_detail.split(" ")
        package_id, weight, distance, coupon = [
            str(list_values[0]),
            int(list_values[1]),
            int(list_values[2]),
            str(list_values[3]),
        ]
        _discounts = Discounts()
        _discounts.add_list_of_discount(discounts.get_discount_by_coupon([coupon]))
        pkg = Package(
            pkg_id=package_id,
            base_cost=base_delivery_price,
            distance=distance,
            weight=weight,
            discounts=_discounts,
        )
        all_packages.add_package(pkg)

    vehicle_count, vehicle_max_speed, vehicle_max_load = vehicle_details
    vehicles = Vehicles()
    vehicles.add_vehicles(vehicle_count, vehicle_max_speed, vehicle_max_load)
    packageGroups = calculate_package_groups(vehicle_max_load, all_packages.packages)

    index = 0
    while True:
        if len(packageGroups.pkg_grp) == index:
            break
        for i in vehicles.vehicles:
            packageGroups.packages[index].set_delivery_time_for_packages(
                i.max_speed, i.next_delivery_time
            )
            i.set_next_delivery_time(
                packageGroups.packages[index].get_total_delivery_time()
            )
            index += 1
        vehicles.sort_vehicles()
    p = packageGroups.convert_to_packages()

    output = ""
    for p in p.packages:
        output += "{} {} {} {}\n".format(
            p.pkg_id, p.discount_cost, p.total_cost, p.delivery_time
        )
    print(output)


if __name__ == "__main__":
    app()
