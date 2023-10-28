from src.item import Item


class LangKeyboard:
    lang = ['EN', 'RU']

    def change_lang(self):
        if self.__language == LangKeyboard.lang[0]:
            self.__language = LangKeyboard.lang[1]
        else:
            self.__language = LangKeyboard.lang[0]


class Keyboard(Item, LangKeyboard):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def __str__(self):
        return self.name

    @property
    def language(self):
        return self.__language
