"""
Generate poker hand rankings pairs, 2 pairs, flushes, and high card.
:param What it is composed of in a hand dealing, the required to generate each of those in a hand dealing.
:return Flushes, two pair, pair, and high card.
"""

from random import randint
import deck


def is_flush(my_hand):
    """
    Determining whether hand is a flush and adding to counter if it is.
    :param my_hand: The player's current hand
    :return: Boolean based on identification of hand
    """
    if all(card.get_suit() == my_hand[0].get_suit() for card in my_hand):
        return True
    else:
        return False


def is_two_pair(my_hand):
    """
    Determining whether hand is a two pair and adding to counter if it is.
    :param my_hand: The player's current hand
    :return: Boolean based on identification of hand
    """
    counts = {}
    for card in my_hand:
        counts[card.get_rank()] = 0

    if len(counts) < 3:
        return True
    elif len(counts) == 3:
        for card in my_hand:
            counts[card.get_rank()] += 1

        if all(counts[item] != 3 for item in counts):
            return True
        else:
            return False
    else:
        return False


def is_pair(my_hand):
    """
    Determining whether hand is a pair and adding to counter if it is.
    :param my_hand: The player's current hand
    :return: Boolean based on identification of hand
    """
    counts = {}
    for card in my_hand:
        counts[card.get_rank()] = 0
    if len(counts) == 4:
        return True
    elif len(counts) == 3:
        for card in my_hand:
            counts[card.get_rank()] += 1

        for item in counts:
            if counts[item] == 3:
                return True
    else:
        return False

# if __name__ == "__main__":
#     deck=[("Ace","hearts"),("7","hearts"),("5","hearts"),("6","hearts"),("4","hearts")]
#     if is_flush(deck) or is_pair(deck) or is_two_pair(deck):
#         hands["hands"]+=1
#     else:
#         hands["High card"]+=1
#         hands["hands"]+=1
#     print(hands)
