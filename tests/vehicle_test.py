from deliveryservice.delivery.vehicle import CollectionOfVehicle, Vehicle


class TestVehicle:
    def test_set_next_delivery_time(self):
        vehicle = Vehicle("V1", 30, 120)
        vehicle.set_next_delivery_time(10)
        assert vehicle.next_delivery_time == 20


class TestCollectionOfVehicle:
    def test_collection_of_vehicles(self):
        collection_of_vehicles = CollectionOfVehicle()
        collection_of_vehicles.add_vehicles(3, 200, 130)
        assert len(collection_of_vehicles) == 3
        collection_of_vehicles.vehicles[0].set_next_delivery_time(10)
        collection_of_vehicles.vehicles[1].set_next_delivery_time(30)
        collection_of_vehicles.vehicles[2].set_next_delivery_time(20)
        assert collection_of_vehicles.vehicles[0].next_delivery_time == 20
        assert collection_of_vehicles.vehicles[1].next_delivery_time == 60
        assert collection_of_vehicles.vehicles[2].next_delivery_time == 40
        collection_of_vehicles.sort_vehicles()
        assert collection_of_vehicles.vehicles[0].next_delivery_time == 20
        assert collection_of_vehicles.vehicles[1].next_delivery_time == 40
        assert collection_of_vehicles.vehicles[2].next_delivery_time == 60
