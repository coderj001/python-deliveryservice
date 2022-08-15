from typing import List

from deliveryservice.delivery.packages import CollectionOfPackage


class PackageGroup:
    pkg_grp: List[CollectionOfPackage]

    def __init__(self):
        self.pkg_grp = []

    def __len__(self) -> int:
        return len(self.pkg_grp)

    def sort_package_group(self) -> None:
        self.pkg_grp = sorted(self.pkg_grp)

    def add_package_group(self, packages: CollectionOfPackage):
        self.pkg_grp.append(packages)

    def add_list_of_package(self, packages: List[CollectionOfPackage]):
        for pkg in packages:
            self.pkg_grp.append(pkg)

    def convert_to_packages(self) -> CollectionOfPackage:
        packages = CollectionOfPackage()
        for i in self.pkg_grp:
            packages.add_list_of_package(i.packages)
        return packages
