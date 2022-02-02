from card import Card
from random import shuffle

class Deck:
    def __init__(self, is_empty=False):
        
        self._cards = []
        if not is_empty:
            self.build()
        

    @property
    def cards(self):
        return self._cards    

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        self._cards = [Card(value, "hearts") for value in range(2, 15)]
        self._cards += [Card(value, "diamonds") for value in range(2, 15)]
        self._cards += [Card(value, "clubs") for value in range(2, 15)]
        self._cards += [Card(value, "spades") for value in range(2, 15)]

    def show(self):
        for card in self.cards:
            card.show()  

    def shuffle(self):
        shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None
        

    def add(self, card):
        self._cards.insert(0,card)

    