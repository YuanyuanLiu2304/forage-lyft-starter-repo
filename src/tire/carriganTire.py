from tire import Tire
class CarrignTire(Tire):

    def __init__(self,tire_wear_sensors:list):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear_sensors )