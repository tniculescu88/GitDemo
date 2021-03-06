from deck import Deck


class Player:
    def __init__(self, name, deckObj, is_computer=False):
        self._name = name
        self._deck = deckObj
        self._is_computer = is_computer

    @property
    def name(self):
        return self._name
    
    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        return self._deck.size == 0

    def draw_card(self):
        if self._deck.size:
            return self._deck.draw()
        else:
            return None
    
    def add_card(self, card):
        if card:
            self._deck.add(card)
