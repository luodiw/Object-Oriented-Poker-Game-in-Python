"""
Arranging the card format of deck.
"""


class Card:
    def __init__(self, rank, suit):
        """
        Create a card object
        :param rank: int from 2-14 denoting rank of card
        :param suit: single character str denoting the suit of card
        """
        self.card = {"rank": rank, "suit": suit}

    def get_rank(self):
        """
        Get rank of card
        :return: rank from dictionary depicting a card
        """
        return self.card["rank"]

    def get_suit(self):
        """
        Get suit of card
        :return: suit from dictionary depicting a card
        """
        return self.card["suit"]

    def __str__(self):
        """
        Formats card for printing
        :return: Formatted card 
        """
        suits = {"H": "hearts", "D": "diamonds", "S": "spades", "C": "clubs"}
        rank = self.get_rank()
        suit = self.get_suit()
        if rank <= 10:
            return f"{rank} of {suits[suit]}"
        elif rank == 11:
            return f"Jack of {suits[suit]}"
        elif rank == 12:
            return f"Queen of {suits[suit]}"
        elif rank == 13:
            return f"King of {suits[suit]}"
        elif rank == 14:
            return f"Ace of {suits[suit]}"


if __name__ == "__main__":
    first = Card(11, "S")
    print(first)
    print(first.get_rank())
    print(first.get_suit())
