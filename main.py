# added dummy submit from Asia Timezone
from player import Player
from deck import Deck
from card import Card
separator = "\t"*7
if __name__ == '__main__':
    # creating the bigDeck of all cards
    bigDeck = Deck(is_empty=False)
    print("Shuffling the cards")
    bigDeck.shuffle()

    # creating 2 players
    print("Creating the players and distributing the cards to each player")
    p1 = Player("Player1", Deck(is_empty=True), is_computer=False)
    p2 = Player("Computer", Deck(is_empty=True), is_computer=True)
    playersList = [p1, p2]
    # distributing the cards from the bigDeck to the 2 players
    for cardIndex in range(int(52/2+1)):
        p1.add_card(bigDeck.draw())
        p2.add_card(bigDeck.draw())

    print("Starting the GAME !!!")
    no_rounds = 1
    print(f"{p1.name}{separator}{p2.name}")
    while not (p1.has_empty_deck() or p2.has_empty_deck()):
        # draw the cards for war
        c1 = p1.deck.draw()
        c2 = p2.deck.draw()
        if c1.value == c2.value:
            print(f"WAR started for {c1.show()} and {c2.show()} !!!")
            raise NotImplementedError("War star")
        elif c1.value > c2.value:
            resultMessage = f"{p1.name} wins round {no_rounds}"
            p1.add_card(c1)
            p1.add_card(c2)
        else:
            resultMessage = f"{p2.name} wins round {no_rounds}"
            p2.add_card(c1)
            p2.add_card(c2)
        no_cards_p1 = p1.deck.size
        no_cards_p2 = p2.deck.size

        print(f"{c1.show()}{separator}{c2.show()}\n{resultMessage}\n{no_cards_p1}{separator}{no_cards_p2}")
        no_rounds += 1
        # input("Press any key to continue")







