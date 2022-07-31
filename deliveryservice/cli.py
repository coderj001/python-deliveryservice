import typer
from typing import Any, List, Optional
from rich.prompt import Prompt
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
        print(package_id, weight, distance, coupon, sep=",")


@app.command(name="time")
def calculateDeliveryTimeEstimation(a: int, b: int):
    pass


if __name__ == "__main__":
    app()
