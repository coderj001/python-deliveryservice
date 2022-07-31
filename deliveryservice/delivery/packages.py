from dataclasses import dataclass
from typing import List

from delivery.package import Package


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

    def length(self) -> int:
        return len(self.packages)

    def swap(self, i: int, j: int):
        self.packages[i], self.packages[j] = self.packages[j], self.packages[i]

    def less(self, i: int, j: int) -> bool:
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
