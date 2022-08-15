from deliveryservice.delivery.discount import (CollectionOfDiscount, Discount,
                                               mock_all_discounts)
from deliveryservice.delivery.package import Package


class TestPackage:
    def test_calculate_delivery_cost_1(self):
        discount = Discount("OFR001", 0, 0, 0, 0, 0)
        discounts = CollectionOfDiscount()
        discounts.add_discount(discount)
        package = Package("PKG1", 100, 5, 5, discounts)
        assert package.is_discount_applicable() == False
        package.calculate_delivery_cost()
        assert package.total_cost == 175

    def test_calculate_delivery_cost_2(self):
        discount = Discount("OFR003", 5, 50, 250, 10, 150)
        discounts = CollectionOfDiscount()
        discounts.add_discount(discount)
        package = Package("PKG1", 100, 100, 10, discounts)
        assert package.is_discount_applicable() == True
        package.calculate_delivery_cost()
        assert package.total_cost == 665
