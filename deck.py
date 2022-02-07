"""
Deck of 52 cards created for shuffling and dealing.
"""

import random
import card


class Deck:
    def __init__(self):
        """
        Create a deck of cards in 4 suits and 13 ranks.
        :return: Generated card objects added to the empty deck list
        """
        suits = ['H', 'D', 'S', 'C']
        self._size = 52
        self.deck = []
        for rank in range(2, 15):
            for suit in suits:
                temp_card = card.Card(rank, suit)
                self.deck.append(temp_card)

    def shuffle_deck(self):
        """
        Shuffling deck of 52 cards 
        :return A shuffled deck 
        """
        random.shuffle(self.deck)

    def deal_card(self):
        """
        Deal a card from deck then remove it
        :return: Dealt card
        """
        if self._size > 0:
            dealt_card = self.deck.pop()
            self._size -= 1
            return dealt_card
        else:
            return None

    def size(self):
        """
        Number of cards remaining in the deck
        :return: size of deck
        """
        return self._size

    def __str__(self):
        """
        Format the deck for printing
        :return: string including card format and deck format
        """
        deck_string = "["
        counter = 0
        if self._size == 0:
            return "[]"
        for card in self.deck:
            if counter == self._size - 1:
                deck_string += f"{card}]"
            else:
                deck_string += f"{card}, "
                counter += 1
        return deck_string


if __name__ == "__main__":
    # print("####################  unshuffled  ########################")
    deck1 = Deck()
    # for x in deck1.deck:
    #     print(x)
    # print("####################  Shuffled  ########################")
    deck1.shuffle_deck()
    # for x in deck1.deck:
    #     print(x)
    print(deck1.deal_card())
    print(deck1.deal_card())
    print(deck1.deal_card())
    print(deck1)
    # for x in deck1.deck:
    #     print(x)
