from datetime import datetime,date
from src.battery.battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date: date,current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        if self.current_date.year - self.last_service_date.year > 3:
            return True
        else:
            return False