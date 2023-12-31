from datetime import date
from src.model.car import Car
from src.engine.capulet_engine import CapuletEngine
from src.engine.sternman_engine import SternmanEngine
from src.engine.willoughby_engine import WilloughbyEngine
from src.battery.spindler_battery import SpindlerBattery
from src.battery.nubbin_battery import NubbinBattery


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_gilssade( current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome( current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex( current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine, battery)
        return car
