from dataclasses import dataclass
from typing import List

from deliveryservice.delivery.package import Package


@dataclass
class Packages:
    packages: List[Package]

    def __init__(self):
        self.packages = []

    def add_package(self, package: Package):
        self.packages.append(package)

    def add_list_of_package(self, packages: List[Package]):
        for pkg in packages:
            self.packages.append(pkg)

    def __len__(self) -> int:
        return len(self.packages)

    # def swap(self, i: int, j: int):
    #     self.packages[i], self.packages[j] = self.packages[j], self.packages[i]

    def __lt__(self, i: int, j: int) -> bool:
        return self.packages[i].weight < self.packages[j].weight

    def getTotalWeight(self) -> int:
        # Get total weight
        ## Iterates through the package and calculates the weight of packages.
        ## returns total weight of the given packages
        return sum([pkg.weight for pkg in self.packages])

    def calculateDeliveryCost(self):
        # Calculate delivery cost
        ## Utiliy method to calculate the delivery cost of the packages.
        ## It also sets the totalCost variable for each Package.

        for pkg in self.packages:
            pkg.calculateDeliveryCost()

    def set_delivery_time_for_packages(self, max_speed: int, additional_time: float):
        for i in self.packages:
            i.delivery_time = round(
                additional_time + float(i.distance) / float(max_speed)
            )

    def getTotalDeliveryTime(self)-> float:
        deliveryTime: float
        for i in self.packages:
            if deliveryTime < i.delivery_time:
                deliveryTime = i.delivery_time

        return deliveryTime

    def containsPackage(self, package: Package)-> bool:
        for pkg in self.packages[0].packages:
            if pkg.pkg_id == package.pkg_id:
                return True
        return False
