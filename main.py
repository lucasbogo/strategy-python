from abc import ABC, abstractmethod

class CalculateShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self, price, weight):
        pass


class CalculateShippingByAir(CalculateShippingStrategy):
    def calculate_shipping(self, price, weight):
        price = 30
        return price * weight * 2

class CalculateShippingByLand(CalculateShippingStrategy):
    def calculate_shipping(self, price, weight):
        price = 20
        return price * weight * 0.5