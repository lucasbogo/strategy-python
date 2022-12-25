from abc import ABC, abstractmethod

class CalculateShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self, price, weight, total):
        pass


class CalculateShippingByAir(CalculateShippingStrategy):
    def calculate_shipping(self, price, weight, total):
        price = 30
        total = price + weight * 2
        return total

class CalculateShippingByLand(CalculateShippingStrategy):
    def calculate_shipping(self, price, weight, total):
        price = 20
        total = price + weight * 0.5
        return total

class Shipping:
    def __init__(self, strategy):
        self._strategy = strategy

    def calculate_shipping(self, price, weight, total):
        return self._strategy.calculate_shipping(price, weight, total)

if __name__ == "__main__":
    shipping = Shipping(CalculateShippingByAir())
    print(shipping.calculate_shipping(10, 2, 0))

    shipping = Shipping(CalculateShippingByLand())
    print(shipping.calculate_shipping(10, 2, 0))

