from src.item import Item


class LangKeyboard:
    lang = ['EN', 'RU']

    def __init__(self):
        self.__language = self.lang[0]

    def change_lang(self):
        if self.__language == self.lang[0]:
            self.__language = self.lang[1]
        else:
            self.__language = self.lang[0]

    @property
    def language(self):
        return self.__language


class Keyboard(Item, LangKeyboard):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LangKeyboard.__init__(self)
