from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return 'Требуется ткани: ' + str(round(self.param / 6.5 + 0.5))


class Suit(Clothes):
    @property
    def tissue_consumption(self):
        return 'Требуется ткани: ' + str(round(2 * self.param + 0.3))


c = Coat(48)
print(c.tissue_consumption)

s = Suit(1.75)
print(s.tissue_consumption)

