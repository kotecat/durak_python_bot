from objects.deck import Deck

deck = Deck()

deck._fill_cards()
print(deck.cards)
print(len(deck.cards))
print(deck.trump)

deck.cards.remove(deck.cards[1])
print(deck.cards)