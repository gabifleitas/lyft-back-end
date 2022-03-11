from car import Car

class CarFactory(Car):
    current_date = int()
    last_service_date = int()
    current_mileage = int()
    last_service_mileage = int()
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        #Create car calliope
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        #Create car glissade
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        #Create car palindrome
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        #Create car rorschach
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        #Create car thovex
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage