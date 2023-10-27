from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float,
                 quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', "
                f"{self.price}, {self.quantity}, {self.__number_of_sim})")

    def __str__(self):
        return super().__str__()

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            return "Это не экземпляры одних классов/надклассов"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim > 0 and isinstance(new_number_of_sim, int):
            self.__number_of_sim = new_number_of_sim
        else:
            print("ValueError: Количество физических "
                  "SIM-карт должно быть целым числом больше нуля.")
