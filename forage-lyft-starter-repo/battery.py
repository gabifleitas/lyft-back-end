from car import Car
from serviceable import Serviceable
from carfactory import CarFactory

#which batteries are going go to be used in the cars
class Battery(Serviceable, CarFactory):
    def splinder_battery(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def nubbin_battery(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date