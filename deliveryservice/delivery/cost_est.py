from typing import List

from deliveryservice.delivery.package import Package
from deliveryservice.delivery.packagegrp import PackageGroup
from deliveryservice.delivery.packages import CollectionOfPackage


def get_possible_packages(
    collection_of_packages: CollectionOfPackage, max_load: int
) -> PackageGroup:
    group = PackageGroup()

    for i in range(0, len(collection_of_packages)):
        package_items = CollectionOfPackage()
        package_items.add_package(collection_of_packages.packages[i])
        j = i
        for j in range(0, len(collection_of_packages)):
            if i == j:
                continue
            if (
                collection_of_packages.packages[j].weight
                + package_items.get_total_weight()
                <= max_load
            ):
                package_items.add_package(collection_of_packages.packages[j])
            else:
                group.add_package_group(package_items)
                package_items = CollectionOfPackage()
                package_items.add_package(collection_of_packages.packages[i])

                if (
                    collection_of_packages.packages[j].weight
                    + package_items.get_total_weight()
                    <= max_load
                ):
                    package_items = CollectionOfPackage()
                    package_items.add_package(collection_of_packages.packages[i])
            group.add_package_group(package_items)
    return group


def calculate_package_groups(max_load: int, packages: List[Package]) -> PackageGroup:
    remaining_packages = CollectionOfPackage()
    remaining_packages.add_list_of_package(packages)

    to_be_delivered_packages = PackageGroup()
    while len(remaining_packages) > 0:
        packages_group = get_possible_packages(remaining_packages, max_load)
        packages_group.sort_package_group()
        remaining_packages = CollectionOfPackage()
        to_be_delivered_packages.add_package_group(packages_group.pkg_grp[0])
        for pkg in packages:
            if not to_be_delivered_packages.convert_to_packages().contains_package(pkg):
                remaining_packages.add_package(pkg)

    return to_be_delivered_packages
