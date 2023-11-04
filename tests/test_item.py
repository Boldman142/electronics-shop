"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from homework_1.main import main
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


def test_calculate_total_prise():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert main() is None


def test_pay_rate():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_name():
    assert item1.name == "Смартфон"
    item1.name = "Телефон"
    assert item1.name == "Телефон"


def test_string_to_number():
    assert Item.string_to_number("8.1") == 8


def test_add():
    assert phone1 + item1 == 25


def test_file_not_found():
    assert Item.instantiate_from_csv() == print('Отсутствует файл item.csv')
