from dataclasses import dataclass

from deliveryservice.delivery.discount import Discounts


@dataclass
class Package:
    pkg_id: str
    distance: int
    weight: int
    base_cost: int
    total_cost: int
    discount_cost: int
    delivery_time: float
    discounts: Discounts

    def __init__(
        self,
        pkg_id: str,
        base_cost: int,
        distance: int,
        weight: int,
        discounts: Discounts,
    ) -> None:
        self.pkg_id = pkg_id
        self.base_cost = base_cost
        self.distance = distance
        self.weight = weight
        self.discounts = discounts
        self.discount_cost = 0
        self.total_cost = 0
        self.delivery_time = 0

    def isDiscountApplicable(self) -> bool:
        # Is discount applicable
        ## Checks whether the package has discount or not based on conditions
        ## 1. package weight should be greater or equals to discount minimun package weight
        ## 2. package weight should be lesser or equals to discount maximum package weight
        ## 4. package distance should be greater or equals to discount minimum package distance
        ## 3. package distance should be lesser or equals to discount maximum package distance

        for discount in self.discounts.__dict__.get("discounts"):
            if (
                discount.min_package_weight <= self.weight
                and discount.min_destination_distance <= self.distance
                and self.distance <= discount.max_destination_distance
            ):
                return True
        return False

    def calculateDeliveryCost(self):
        # Calculate Delivery Cost
        ## Calculates delivery cost of the package and if there is any discount, it will be discounted from the totalCost of package.
        ## Formulae:
        ## totalCost_of_Package = (base_cost + (package_weight * 10) + (package_distance * 5)) - discountPrice

        totalCost = self.base_cost + (self.weight * 10) + (self.distance * 5)
        if self.isDiscountApplicable():
            self.discount_cost = self.discounts.calculateDiscountAmount(totalCost)
        self.total_cost = int(totalCost - self.discount_cost)