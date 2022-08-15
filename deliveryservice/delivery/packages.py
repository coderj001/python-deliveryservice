from functools import total_ordering
from typing import List

from deliveryservice.delivery.package import Package


@total_ordering
class CollectionOfPackage:
    packages: List[Package]

    def __init__(self) -> None:
        self.packages = []

    def __len__(self) -> int:
        return len(self.packages)

    def __lt__(self, obj) -> bool:
        if len(self.packages) == len(obj.packages):
            return self.get_total_weight() < obj.get_total_weight()
        return len(self.packages) < len(self.packages)

    def __gt__(self, obj):
        if len(self.packages) == len(obj.packages):
            return self.get_total_weight() > obj.get_total_weight()
        return len(self.packages) > len(self.packages)

    def __le__(self, obj):
        if len(self.packages) == len(obj.packages):
            return self.get_total_weight() <= obj.get_total_weight()
        return len(self.packages) < len(self.packages)

    def __ge__(self, obj):
        if len(self.packages) == len(obj.packages):
            return self.get_total_weight() >= obj.get_total_weight()
        return len(self.packages) > len(self.packages)

    def __eq__(self, obj):
        if len(self.packages) == len(obj.packages):
            return self.get_total_weight() == obj.get_total_weight()

    def sort_packages(self) -> None:
        self.packages = sorted(self.packages)

    def add_package(self, package: Package) -> None:
        self.packages.append(package)

    def add_list_of_package(self, packages: List[Package]) -> None:
        for pkg in packages:
            self.packages.append(pkg)

    def get_total_weight(self) -> int:
        return sum([pkg.weight for pkg in self.packages])

    def calculate_delivery_cost(self):
        for pkg in self.packages:
            pkg.calculate_delivery_cost()

    def set_delivery_time_for_packages(
        self, max_speed: int, additional_time: float
    ) -> None:
        for i in self.packages:
            i.delivery_time = round(
                additional_time + float(i.distance) / float(max_speed)
            )

    def get_total_delivery_time(self) -> float:
        delivery_time: float = 0
        for pkg in self.packages:
            if delivery_time < pkg.delivery_time:
                delivery_time = pkg.delivery_time

        return delivery_time

    def contains_package(self, package: Package) -> bool:
        for pkg in self.packages:
            if pkg.pkg_id == package.pkg_id:
                return True
        return False
