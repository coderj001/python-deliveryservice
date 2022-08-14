from typing import List

from deliveryservice.delivery.packages import CollectionOfPackage


class PackageGroup:
    pkg_grp: List[CollectionOfPackage]

    def __init__(self):
        self.pkg_grp = []

    def add_package_group(self, packages: CollectionOfPackage):
        self.pkg_grp.append(packages)

    def add_list_of_package(self, packages: List[CollectionOfPackage]):
        for pkg in packages:
            self.pkg_grp.append(pkg)

    def __len__(self) -> int:
        return len(self.pkg_grp)

    # def swap(self, i: int, j: int):
    #     self.pkg_grp[i], self.pkg_grp[j] = self.pkg_grp[j], self.pkg_grp[i]

    def __lt__(self, i: int, j: int) -> bool:
        return self.pkg_grp[i].get_total_weight() < self.pkg_grp[j].get_total_weight()

    def convert_to_packages(self) -> CollectionOfPackage:
        packages = CollectionOfPackage()
        for i in self.pkg_grp:
            packages.add_package(i)
        return packages
