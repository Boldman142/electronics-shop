from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 25)
phone1 = Phone("iPhone 14", 120_000, 10, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 10, 2)"


def test_str():
    assert str(phone1) == 'iPhone 14'


def test_add():
    assert phone1 + item1 == 35
    assert print(phone1 + 10) == print("Это не экземпляры"
                                       " одних классов/надклассов")


def test_number_of_sim():
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
