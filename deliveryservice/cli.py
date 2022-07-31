from typing import List, Optional

import typer
from delivery.discount import Discounts, mockAllDiscounts
from delivery.package import Package
from delivery.packages import Packages
from rich import print

app = typer.Typer()


@app.command(name="cost", help="Find delivery cost for packages")
def findDeliveryCostForPackages(
    base_delivery_price: int = typer.Argument(default=None, help="Base delivery price"),
    total_packages: Optional[int] = typer.Argument(
        default=1, help="Total number of packages"
    ),
):
    # find delivery cost for packages
    all_packages = Packages()
    discounts = mockAllDiscounts()

    print(base_delivery_price, total_packages, sep=",")
    print("Enter package_id, weight, distance, coupon (with space)")
    for _ in range(0, total_packages):
        values = input()
        list_values: List[str | int] = values.split(" ")
        package_id, weight, distance, coupon = (
            str(list_values[0]),
            int(list_values[1]),
            int(list_values[2]),
            str(list_values[3]),
        )
        # print(package_id, weight, distance, coupon, sep=",")
        _discounts = Discounts()
        _discounts.add_list_of_discount(discounts.getDiscountByCoupon([coupon]))
        pkg = Package(
            pkg_id=package_id,
            base_cost=base_delivery_price,
            distance=distance,
            weight=weight,
            discounts=_discounts,
        )
        all_packages.add_package(pkg)
    all_packages.calculateDeliveryCost()
    output = ""
    for pkg in all_packages.__dict__.get("packages", []):
        output += "{} {} {}\n".format(
            pkg.pkg_id, pkg.discount_cost, pkg.total_cost
        )
    print(output)


@app.command(name="time")
def calculateDeliveryTimeEstimation():
    pass


if __name__ == "__main__":
    app()
