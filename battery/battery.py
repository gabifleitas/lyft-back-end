from abc import ABC

#which batteries are going go to be used in the cars
class Battery(ABC):
    def needs_service(self):
        pass