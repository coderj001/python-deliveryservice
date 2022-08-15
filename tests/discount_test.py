from deliveryservice.delivery.discount import CollectionOfDiscount, Discount


class TestDiscount:
    def test_calculate_discount_amount(self):
        discount = Discount("0FR002", 7, 50, 150, 100, 250)
        assert discount.calculate_discount_amount(100) == 7

class TestCollectionOfDiscount:
    def test_calculate_discount_amount(self):
        discount1 = Discount("0FR001", 7, 50, 150, 100, 250)
        collection_of_discount = CollectionOfDiscount()
        collection_of_discount.add_discount(discount1)
        assert len(collection_of_discount) == 1
        discount2 = Discount("0FR002", 8, 51, 154, 90, 150)
        collection_of_discount.add_discount(discount2)
        assert len(collection_of_discount) == 2
        total_discount_amount=collection_of_discount.calculate_discount_amount(cost=100)
        assert total_discount_amount == 15

    def test_get_discount_by_coupons(self):
        discount1 = Discount("0FR001", 7, 50, 150, 100, 250)
        discount2 = Discount("0FR002", 8, 51, 154, 90, 150)
        collection_of_discount = CollectionOfDiscount()
        collection_of_discount.add_list_of_discount([discount1, discount2])
        assert len(collection_of_discount) == 2
        coupon_discounts = collection_of_discount.get_discount_by_coupon(["0FR001"])
        assert len(coupon_discounts) == 1
        assert coupon_discounts[0].coupon == "0FR001"
