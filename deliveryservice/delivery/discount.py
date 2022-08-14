from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Discount:
    coupon: str
    percentage: int
    min_destination_distance: int
    max_destination_distance: int
    min_package_weight: int
    max_package_weight: int

    def __init__(
        self,
        coupon: str,
        percentage: int,
        min_destination_distance: int,
        max_destination_distance: int,
        min_package_weight: int,
        max_package_weight: int,
    ) -> None:
        self.coupon = coupon
        self.percentage = percentage
        self.min_destination_distance = min_destination_distance
        self.max_destination_distance = max_destination_distance
        self.min_package_weight = min_package_weight
        self.max_package_weight = max_package_weight

    def calculateDiscountAmount(self, cost: int) -> int:
        return int(cost / 100 * self.percentage)


@dataclass
class CollectinOfDiscount:
    discounts: List[Discount]

    def __init__(self) -> None:
        self.discounts = []

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)

    def add_list_of_discount(self, discounts: List[Discount]):
        for discount in discounts:
            self.add_discount(discount)

    def calculate_discount_amount(self, cost: int) -> int:
        total_discount_amount: int = 0
        for i in self.discounts:
            total_discount_amount += i.calculateDiscountAmount(cost)
        return total_discount_amount

    def get_discount_by_coupon(self, coupons: List[str]) -> List[Discount]:
        discounts: List[Discount] = []
        for discount in self.discounts:
            if discount.coupon in coupons:
                discounts.append(discount)
        return discounts


coupons: Dict[str, str] = {
    "coupon1": "OFR001",
    "coupon2": "OFR002",
    "coupon3": "OFFR002",
    "coupon4": "OFR003",
}


def mock_all_discounts() -> CollectinOfDiscount:
    allDiscounts = CollectinOfDiscount()
    allDiscounts.add_discount(Discount("OFR001", 10, 0, 200, 70, 200))
    allDiscounts.add_discount(Discount("OFR002", 7, 50, 150, 100, 250))
    allDiscounts.add_discount(Discount("OFFR002", 7, 50, 150, 100, 250))
    allDiscounts.add_discount(Discount("OFR003", 5, 50, 250, 10, 150))
    return allDiscounts
