"""
PLaying poker hands for the user to compare which hand wins. Points are cumulative for the plays.
"""

import deck
from hand_rankings import *
from card import *


class PokerHand:
    def __init__(self, initial_hand):
        """
        Constructor for PokerHand object, initializes hand attribute 
        :param self: Object being created
        :param initial_hand: list of cards taken as initial hand 
        :return: hand object containing hand, hand ranking, and size
        """
        self.hand = initial_hand
        self.hand_ranking = None
        self._size = 5

    def add_card(self, card):
        """
        Adds a card to the hand
        :param self: The hand to add card to
        :return: a card is added to hand
        """
        if self._size < 5:
            self.hand.append(card)
            self._size += 1
        else:
            return "Hand is full"

    def discard_hand(self):
        """
        Resets hand to an empty one
        :param self: The hand to reset
        :return: an empty hand
        """
        self.hand = []
        self._size = 0

    def get_ith_card(self, index):
        """
        Gets card in the hand from a certain index
        :param self: The hand to extract the card from
        :return: a card object at the index given
        """
        if index < 0 or index > self._size:
            return "invalid index"
        else:
            return self.hand[index]

    def get_hand_ranking(self):
        """
        Gets general hand ranking (flush, two pair, pair, high card)
        :param self: The hand to extract information from
        :return: an integer from 1-4 that identifies the generalized type of hand
        """
        if is_flush(self.hand):
            self.hand_ranking = 4
            return self.hand_ranking
        elif is_two_pair(self.hand):
            self.hand_ranking = 3
            return self.hand_ranking
        elif is_pair(self.hand):
            self.hand_ranking = 2
            return self.hand_ranking
        else:
            self.hand_ranking = 1
            return self.hand_ranking

    def get_rank_count(self):
        """
        Gets all ranks in hand and how many times they appear
        :param self: The hand to extract information from
        :return: a dictionary with all ranks in the hand and their count
        """
        my_hand_counts = {}
        for card in self.hand:
            my_hand_counts[card.get_rank()] = 0
        for card in self.hand:
            my_hand_counts[card.get_rank()] += 1
        return my_hand_counts

    def get_max_rank(self, hand_count):
        """
        Gets the highest rank in hand (when sorted by count)
        :param self: The hand to extract information from
        :return: the highest rank that appears the most
        """
        max_rank = 0
        max_count = 0
        for rank in hand_count:
            if hand_count[rank] > max_count:
                max_rank = rank
                max_count = hand_count[rank]
            elif hand_count[rank] == max_count:
                if rank > max_rank:
                    max_rank = rank
        return max_rank

    def compare_to(self, other_hand):
        """
        Determines which of two poker hands is worth more. Returns an int
        which is either positive, negative, or zero depending on the comparison.
        :param self: The first hand to compare
        :param other_hand: The second hand to compare
        :return: a negative number if self is worth LESS than other_hand,
        zero if they are worth the SAME (a tie), and a positive number if
        self is worth MORE than other_hand
        """
        # Check if hands have same ranking
        if self.get_hand_ranking() == other_hand.get_hand_ranking():
            my_count = self.get_rank_count()
            other_count = other_hand.get_rank_count()

            if len(my_count) < len(other_count):
                comparison_range = len(my_count)
            else:
                comparison_range = len(other_count)

            for comparison in range(comparison_range):
                my_max_rank = self.get_max_rank(my_count)

                other_max_rank = other_hand.get_max_rank(other_count)
                my_count.pop(my_max_rank)
                other_count.pop(other_max_rank)

                if my_max_rank > other_max_rank:
                    return 1
                elif my_max_rank < other_max_rank:
                    return -1

            return 0

        else:
            # if the generalized ranking is not the same return the difference
            return self.hand_ranking - other_hand.hand_ranking

    def __str__(self):
        """
        Format the hand for printing
        :return: string including hand format
        """
        hand_string = "["
        counter = 0
        if self._size == 0:
            return "[]"
        for card in self.hand:
            if counter == self._size - 1:
                hand_string += f"{card}]"
            else:
                hand_string += f"{card}, "
                counter += 1
        return hand_string


def main(playing_deck):
    """
    Runs the game menu and handles when to compare hands as well as dealing new hands
    :param playing_deck: Shared deck of cards between both 
    :return: output to screen showing win or lose
    """
    deck = playing_deck
    deck.shuffle_deck()
    hand1_initial = []
    hand2_initial = []
    for card in range(5):
        hand1_initial.append(deck.deal_card())
        hand2_initial.append(deck.deal_card())
    hand1 = PokerHand(hand1_initial)
    hand2 = PokerHand(hand2_initial)
    points = 0
    game_round = 1
    while True:
        if game_round == 1:
            print("Welcome to How Does it Rank?")
        print("****************************")
        print(f"Hand 1: {hand1}")
        print(f"Hand 2: {hand2}")
        choices = "012"
        user_choice = input("Which hand is bigger (1 or 2) or is it a tie (0)? ")
        while (user_choice not in choices) or len(user_choice) != 1:
            user_choice = input("Please enter a valid integer (0, 1, or 2): ")
        user_choice = int(user_choice)

        if hand1.compare_to(hand2) >= 1:
            outcome = 1
        elif hand1.compare_to(hand2) < 0:
            outcome = 2
        elif hand1.compare_to(hand2) == 0:
            outcome = 0

        if outcome == user_choice:
            points += 1
            print("Congratulations! you win this round!")
            print(f"Your points:{points}")
        else:
            print(f"You lost on round {game_round}, better luck next time")
            if outcome == 0:
                print("The correct answer was a draw")
            elif outcome == 1:
                print("The correct answer was hand 1")
            elif outcome == 2:
                print("The correct answer was hand 2")
            print(f"Your points:{points}")
            return

        if deck._size < 10:
            print(f"No cards remaining! game ending after {game_round} rounds")
            return
        else:
            hand1.discard_hand()
            hand2.discard_hand()
            for card in range(5):
                hand1.add_card(deck.deal_card())
                hand2.add_card(deck.deal_card())
        game_round += 1


if __name__ == "__main__":
    playing_deck = deck.Deck()
    # #playing_deck.shuffle_deck()
    # hand1=PokerHand(playing_deck)
    # hand2=PokerHand(playing_deck)
    # for x in range(5):
    #     hand1.add_card(playing_deck.deal_card())
    #     hand2.add_card(playing_deck.deal_card())
    # print(hand1)
    # print(hand2)
    # print(hand1.compare_to(hand2))
    main(playing_deck)
    # hand1=PokerHand([Card(4,"C"),Card(12,"H"),Card(12,"H"),Card(5,"H"),Card(14,"H")])
    # hand2=PokerHand([Card(5,"S"),Card(12,"S"),Card(12,"S"),Card(14,"C"),Card(2,"S")])
    # print(hand1.compare_to(hand2))
