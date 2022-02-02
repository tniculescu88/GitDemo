from player import Player
from deck import Deck

if __name__ == '__main__':
    d1 = Deck(52)
    d1.build()
    # d1.show()
    print("Shuffling the cards")
    d1.shuffle()
    print(f"len(d1.cards) = {len(d1.cards)}   len(d1._cards) = {len(d1._cards)}")
    assert len(d1.cards) == 52, "len(d1.cards) should be 52 and it is {%s}"%(len(d1.cards))
    # d1.show()
    print("Creating the players and distributing the cards to each player")
    p1 = Player("Player1", d1, False)
    p2 = Player("Computer", d1, True)
    p1.show_cards()
    p2.show_cards()
    # while p1.has_empty_deck() or p2.has_empty_deck():
    #     break
