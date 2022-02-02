class Suit:
    
    MEANING = {"hearts":"♥", "diamonds":"♦", "clubs":"♣", "spades":"♠"}
    
    def __init__(self, description):
        self._description = description
        self._symbol = Suit.MEANING[self._description]

    @property
    def description(self):
        return self._description
    
    @property
    def symbol(self):
        return self._symbol

    