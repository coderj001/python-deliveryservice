from functools import total_ordering
from typing import List


@total_ordering
class Vehicle:
    vehicle_id: int
    max_speed: int
    max_load: int
    next_delivery_time: float

    def __init__(self, vehicle_id, max_speed, max_load):
        self.vehicle_id = vehicle_id
        self.max_load = max_load
        self.max_speed = max_speed
        self.next_delivery_time = 0

    def __lt__(self, obj) -> bool:
        return self.next_delivery_time < obj.next_delivery_time

    def set_next_delivery_time(self, total_delivery_time: float):
        self.next_delivery_time = round(2 * total_delivery_time)


class CollectionOfVehicle:
    vehicles: List[Vehicle]

    def __init__(self) -> None:
        self.vehicles = []

    def __len__(self) -> int:
        return len(self.vehicles)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def add_list_of_vehicle(self, vehicles: List[Vehicle]):
        for v in vehicles:
            self.vehicles.append(v)

    def add_vehicles(self, vehicle_count, vehicle_max_speed, vehicle_max_load):
        for i in range(0, vehicle_count):
            self.vehicles.append(
                Vehicle(
                    vehicle_id=i,
                    max_speed=vehicle_max_speed,
                    max_load=vehicle_max_load,
                )
            )

    def sort_vehicles(self) -> List[Vehicle]:
        self.vehicles = sorted(self.vehicles)
