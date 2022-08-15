from deliveryservice.delivery.discount import Discount


class TestDiscount:
    def test_calculate_discount_amount(self):
        discount = Discount("0FR002", 7, 50, 150, 100, 250)
        assert discount.calculate_discount_amount(100) == 7
