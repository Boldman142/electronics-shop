import pytest
from src.keyboard import Keyboard


def test_init_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_setter_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = "DU"


def test_change_lang():
    new_kb = Keyboard("name", 1000, 3)
    assert new_kb.language == "EN"
    new_kb.change_lang()
    assert new_kb.language == "RU"
    new_kb.change_lang()
    assert new_kb.language == "EN"
