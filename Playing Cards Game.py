from random import shuffle


class Card:
    """
    Represents a playing card.

    Attributes:
        suit (str): The suit of the card (e.g., "Clubs", "Diamonds", "Hearts", "Spades").
        value (int): The value of the card (2-14).
        name (str): The name of the card (e.g., "2", "3", ..., "10", "Jack", "Queen", "King", "Ace").
    """

    def __init__(self, value, suit):
        """
        Initializes a Card instance.

        Args:
            value (int): The value of the card (2-14).
            suit (str): The suit of the card (e.g., "Clubs", "Diamonds", "Hearts", "Spades").
        """
        self.suit = suit
        self.value = value
        self.name = str(value) if 2 <= value <= 10 else {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}[value]

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: The string representation of the card.
        """
        return f"{self.name} of {self.suit}"


class Deck:
    """
    Represents a deck of cards.

    Attributes:
        cards (list): The list of Card instances representing the deck of cards.
    """

    def __init__(self):
        """Initializes a Deck instance."""
        self.cards = []

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = list(range(2, 15))

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

        shuffle(self.cards)

    def draw(self):
        """
        Draws a card from the deck.

        Returns:
            Card: The Card instance that is drawn.

        Raises:
            RuntimeError: If the deck is empty and there are no cards left to draw.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise RuntimeError("The deck is empty.")


if __name__ == "__main__":
    deck = Deck()

    # Draw and print 5 cards
    for _ in range(5):
        card = deck.draw()
        print(card)
