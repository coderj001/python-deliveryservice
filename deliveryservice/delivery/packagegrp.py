from typing import List

from deliveryservice.delivery.packages import Packages


class PackageGroup:
    pkg_grp: List[Packages]

    def __init__(self):
        self.pkg_grp=[]

    def add_package_group(self, packages: Packages):
        self.pkg_grp.append(packages)

    def add_list_of_package(self, packages: List[Packages]):
        for pkg in packages:
            self.pkg_grp.append(pkg)

    def __len__(self) -> int:
        return len(self.pkg_grp)

    # def swap(self, i: int, j: int):
    #     self.pkg_grp[i], self.pkg_grp[j] = self.pkg_grp[j], self.pkg_grp[i]

    def __lt__(self, i: int, j: int) -> bool:
        return self.pkg_grp[i].getTotalWeight() < self.pkg_grp[j].getTotalWeight()

    def convertToPackages(self)->Packages:
        packages = Packages()
        for i in self.pkg_grp:
            packages.add_package(i)
        return packages
