# import random module so we can use shuffle to shuffle the deck of cards.
from random import shuffle


# The class representing a card.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}."


# The class representing a deck of cards.
class Deck:
    def __init__(self):
        # Lists of card values and suits.
        card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        # List comprehension to create list of all 52 combinations of cards stored in self.cards.
        self.cards = [Card(value, suit) for suit in card_suit for value in card_value]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        """Returns the amount of cards in the deck."""
        return len(self.cards)

    def _deal(self, num):
        """Deals the specified number of cards."""
        # Gets the current amount of cards in the deck.
        count = self.count()
        # Sets the maximum amount of cards that can be dealt based on current cards in the deck.
        actual = min([count, num])
        # If there are no cards left in the deck to deal, throw a value error.
        if count == 0:
            raise ValueError("All cards have been dealt")
        # Use a slice to remove number of cards (actual) from the end of the deck.
        cards = self.cards[-actual:]
        # Update the cards in the deck to not include the cards that were previously "sliced" off the end.
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        """Returns a single card. Have to specify [0] to not get a list of a single card."""
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """Returns a list of cards dealt."""
        return self._deal(hand_size)

    def shuffle(self):
        """Shuffles the deck of cards."""
        # If the deck has less than 52 cards, throw a value error.
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


# Create an instance of a deck.
d = Deck()
# Shuffle the deck.
d.shuffle()
# Deal a single card and store in card variable.
card = d.deal_card()
print(card)
# Deal a hand of cards specified and save in hand variable.
hand = d.deal_hand(5)
print(hand)






