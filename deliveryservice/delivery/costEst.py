from typing import List

from deliveryservice.delivery.package import Package
from deliveryservice.delivery.packagegrp import PackageGroup
from deliveryservice.delivery.packages import Packages


def calculatePakcageGroups(max_load: int, packages: List[Package]) -> PackageGroup:
    remainingPackages = Packages()
    remainingPackages.add_list_of_package(packages)

    def getPossiablePackages(packages: Packages) -> PackageGroup:
        group = PackageGroup()

        for i in range(0, len(packages)):
            packageItems = Packages()
            packageItems.add_package(packages.packages[i])
            j = i
            for j in range(0, len(packages)):
                if i == j:
                    continue
                if (
                    packages.packages[j].weight + packageItems.getTotalWeight()
                    <= max_load
                ):
                    packageItems.add_package(packages.packages[j])
                else:
                    group.add_package_group(packageItems)
                    packageItems = Packages()
                    packageItems.add_package(packages.packages[i])

                    if (
                        packages.packages[j].weight + packageItems.getTotalWeight()
                        <= max_load
                    ):
                        packageItems = Packages()
                        packageItems.add_package(packages.packages[i])
                group.add_package_group(packageItems)
        return group

    toBeDeliveredPackages = PackageGroup()
    while True:
        if len(remainingPackages.packages) == 0:
            break
        packagesGroup = getPossiablePackages(remainingPackages)
        remainingPackages = Packages()
        if len(packagesGroup.pkg_grp) > 0:
            toBeDeliveredPackages.add_package_group(packagesGroup.pkg_grp[0])
        for pkg in packages:
            if not toBeDeliveredPackages.convertToPackages().containsPackage(pkg):
                remainingPackages.add_package(pkg)

    return toBeDeliveredPackages
