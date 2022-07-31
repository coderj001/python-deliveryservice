from dataclasses import dataclass
from typing import List, Dict


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
        return cost / 100 * self.percentage


@dataclass
class Discounts:
    discounts: List[Discount]

    def __init__(self) -> None:
        self.discounts = []

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)

    def calculateDiscountAmount(self, cost: int) -> int:
        totalDiscountAmount: int = 0
        for i in self.discounts:
            totalDiscountAmount += i.calculateDiscountAmount(cost)
        return totalDiscountAmount

    def getDiscountByCoupon(self, coupons: List[str]) -> List[Discount]:
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


def MockAllDiscounts() -> List[Discount]:
    allDiscounts: List[Discount] = []
    allDiscounts.append(
        Discount(coupons=coupons.get(coupons.get("coupon1"), 10, 0, 200, 70, 200))
    )
    allDiscounts.append(
        Discount(coupons=coupons.get(coupons.get("coupon2"), 7, 50, 150, 100, 250))
    )
    allDiscounts.append(
        Discount(coupons=coupons.get(coupons.get("coupon3"), 7, 50, 150, 100, 250))
    )
    allDiscounts.append(
        Discount(coupons=coupons.get(coupons.get("coupon4"), 5, 50, 250, 10, 150))
    )
    return allDiscounts
