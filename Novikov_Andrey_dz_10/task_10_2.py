from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__()
        self.name = name
        self.v = v

    @property
    def fabric_consumption(self):
        return round(self.v/6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__()
        self.name = name
        self.h = h

    @property
    def fabric_consumption(self):
        return round(2 * self.h + 0.3, 2)


test_coat = Coat('test coat', 10)
test_suit = Suit('test suit', 3)
print(test_coat.name, test_coat.fabric_consumption)
print(test_suit.name, test_suit.fabric_consumption)
