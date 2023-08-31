from tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, tire_wear_sensors: list):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self) -> bool:
        return sum(self.tire_wear_sensors) >= 3
