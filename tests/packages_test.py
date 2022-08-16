import pytest

from deliveryservice.delivery.discount import CollectionOfDiscount, Discount
from deliveryservice.delivery.package import Package
from deliveryservice.delivery.packages import CollectionOfPackage


@pytest.fixture
def collection_of_packages():
    discount = Discount("OFR001", 0, 0, 0, 0, 0)
    discounts = CollectionOfDiscount()
    discounts.add_discount(discount)
    pk1 = Package("PKG1", 100, 5, 5, discounts)

    discount = Discount("OFR002", 0, 0, 0, 0, 0)
    discounts = CollectionOfDiscount()
    discounts.add_discount(discount)
    pk2 = Package("PKG2", 100, 10, 15, discounts)

    coll_of_pkgs = CollectionOfPackage()
    coll_of_pkgs.add_list_of_package([pk1, pk2])
    return coll_of_pkgs


class TestCollectionOfPackage:
    def test_get_total_wight(self, collection_of_packages):
        assert len(collection_of_packages) == 2
        assert collection_of_packages.get_total_weight() == 20

    def test_calculate_delivery_cost(self, collection_of_packages):
        collection_of_packages.calculate_delivery_cost()
        assert collection_of_packages.packages[0].total_cost == 175
        assert collection_of_packages.packages[1].total_cost == 300

    def test_get_total_delivery_time(self, collection_of_packages):
        assert collection_of_packages.get_total_delivery_time() == 0
        collection_of_packages.set_delivery_time_for_packages(
            max_speed=10, additional_time=0
        )
        assert collection_of_packages.get_total_delivery_time() == 1
