import csv
import os
from math import trunc


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за
        единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return "Это не экземпляры одних классов/надклассов"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость
        конкретного
        товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[0:10]
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all = []
        path_part = path.split("/")
        path_file = os.path.join("..", path_part[0], path_part[1])
        with open(path_file, encoding='windows-1251', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for new in reader:
                name, price, quantity = dict.values(new)
                Item(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        return trunc(float(string))
