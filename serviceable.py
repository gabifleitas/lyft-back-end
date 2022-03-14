from abc import ABC, abstractmethod


class Serviceable(ABC):
    @staticmethod
    def needs_service(self):
        pass