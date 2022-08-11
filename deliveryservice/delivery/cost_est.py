from typing import List

from deliveryservice.delivery.package import Package
from deliveryservice.delivery.packagegrp import PackageGroup
from deliveryservice.delivery.packages import Packages

def get_possible_packages(packages: Packages, max_load: int) -> PackageGroup:
    group = PackageGroup()

    for i in range(0, len(packages)):
        package_items = Packages()
        package_items.add_package(packages.packages[i])
        j = i
        for j in range(0, len(packages)):
            if i == j:
                continue
            if (
                packages.packages[j].weight + package_items.get_total_weight()
                <= max_load
            ):
                package_items.add_package(packages.packages[j])
            else:
                group.add_package_group(package_items)
                package_items = Packages()
                package_items.add_package(packages.packages[i])

                if (
                    packages.packages[j].weight + package_items.get_total_weight()
                    <= max_load
                ):
                    package_items = Packages()
                    package_items.add_package(packages.packages[i])
            group.add_package_group(package_items)
    return group

def calculate_package_groups(max_load: int, packages: List[Package]) -> PackageGroup:
    remaining_packages = Packages()
    remaining_packages.add_list_of_package(packages)

    to_be_delivered_packages = PackageGroup()
    while True:
        if len(remaining_packages.packages) == 0:
            break
        packages_group = get_possible_packages(remaining_packages, max_load)
        remaining_packages = Packages()
        if len(packages_group.pkg_grp) > 0:
            to_be_delivered_packages.add_package_group(packages_group.pkg_grp[0])
        for pkg in packages:
            if not to_be_delivered_packages.convert_to_packages().contains_package(pkg):
                remaining_packages.add_package(pkg)

    return to_be_delivered_packages
