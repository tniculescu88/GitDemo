from suit import Suit


class Card:

    SPECIAL_CARDS_MEANING = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}

    def __init__(self, value, suitDescription):
        self._suit = Suit(suitDescription)
        self._value = value

    @property
    def value(self):
        return self._value

    def is_special(self):
        return self.value in Card.SPECIAL_CARDS_MEANING
                
    def show(self):
        if self.is_special():
            print(f"{Card.SPECIAL_CARDS_MEANING[self._value]} of {self._suit.symbol}")
        else:
            print(f"{self._value} of {self._suit.symbol} ")

