# added dummy submit from Asia Timezone
from player import Player
from deck import Deck

if __name__ == '__main__':
    # creating the bigDeck of all cards
    bigDeck = Deck(is_empty=False)
    print("Shuffling the cards")
    bigDeck.shuffle()

    # creating 2 players
    print("Creating the players and distributing the cards to each player")
    p1 = Player("Player1", Deck(is_empty=True), is_computer=False)
    p2 = Player("Computer", Deck(is_empty=True), is_computer=True)
    # distributing the cards from the bigDeck to the 2 players
    for cardIndex in range(int(52/2+1)):
        p1.add_card(bigDeck.draw())
        p2.add_card(bigDeck.draw())

    print("Will continue")
