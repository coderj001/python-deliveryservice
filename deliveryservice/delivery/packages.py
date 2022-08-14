from dataclasses import dataclass
from typing import List

from deliveryservice.delivery.package import Package


@dataclass
class CollectionOfPackage:
    packages: List[Package]

    def __init__(self):
        self.packages = []

    def add_package(self, package: Package):
        self.packages.append(package)

    def add_list_of_package(self, packages: List[Package]):
        for pkg in packages:
            self.packages.append(pkg)

    def get_total_weight(self) -> int:
        # Get total weight
        ## Iterates through the package and calculates the weight of packages.
        ## returns total weight of the given packages
        return sum([pkg.weight for pkg in self.packages])

    def calculate_delivery_cost(self):
        # Calculate delivery cost
        ## Utiliy method to calculate the delivery cost of the packages.
        ## It also sets the totalCost variable for each Package.

        for pkg in self.packages:
            pkg.calculate_delivery_cost()

    def set_delivery_time_for_packages(self, max_speed: int, additional_time: float):
        for i in self.packages:
            i.delivery_time = round(
                additional_time + float(i.distance) / float(max_speed)
            )

    def get_total_delivery_time(self) -> float:
        delivery_time: float
        for i in self.packages:
            if delivery_time < i.delivery_time:
                delivery_time = i.delivery_time

        return delivery_time

    def contains_package(self, package: Package) -> bool:
        for pkg in self.packages[0].packages:
            if pkg.pkg_id == package.pkg_id:
                return True
        return False
