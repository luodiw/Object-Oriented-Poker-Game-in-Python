from poker_hand import *
from testing import *

""" compare_to method unit tests start below """


def test_equal_hands():
    """
    Tests two identical hands
    """
    hand1 = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    hand2 = PokerHand([Card(14, "S"), Card(13, "S"), Card(12, "S"), Card(11, "S"), Card(10, "S")])
    actual = hand1.compare_to(hand2)
    expect = 0
    assert_equals("Comparing two equal flushes", expect, actual)


def test_first_card_lower():
    """
    Testing same hand type but different rank for first none-pair card
    """
    hand1 = PokerHand([Card(14, "H"), Card(14, "C"), Card(6, "H"), Card(2, "H"), Card(5, "H")])
    hand2 = PokerHand([Card(14, "S"), Card(14, "D"), Card(7, "S"), Card(2, "S"), Card(5, "S")])
    actual = hand1.compare_to(hand2)
    expect = -1
    assert_equals("Comparing two equal pairs with different first card", expect, actual)


def test_same_type_rank_higher():
    """
    Testing same hand type but different rank for main part of hand
    """
    hand1 = PokerHand([Card(11, "H"), Card(11, "C"), Card(11, "D"), Card(2, "H"), Card(2, "S")])
    hand2 = PokerHand([Card(10, "S"), Card(10, "D"), Card(10, "H"), Card(10, "C"), Card(5, "S")])
    actual = hand1.compare_to(hand2)
    expect = 1
    assert_equals("Comparing full house and four-of-a-kind", expect, actual)


def test_fourth_card_lower():
    """
    Testing same hand type but different rank for last card
    """
    hand1 = PokerHand([Card(11, "H"), Card(3, "C"), Card(5, "D"), Card(8, "H"), Card(6, "S")])
    hand2 = PokerHand([Card(11, "S"), Card(4, "D"), Card(5, "H"), Card(8, "C"), Card(6, "D")])
    actual = hand1.compare_to(hand2)
    expect = -1
    assert_equals("Comparing two equal high cards with different last card", expect, actual)


def test_compare_to():
    """ 
    all compare_to tests
    """
    start_tests("compare_to testing")
    test_equal_hands()
    test_first_card_lower()
    test_same_type_rank_higher()
    test_fourth_card_lower()
    finish_tests()


""" get_hand_ranking method unit tests start below """


def test_royal_flush():
    """
    Testing a royal flush hand
    """

    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    actual = hand.get_hand_ranking()
    expect = 4
    assert_equals("Getting rank of royal flush", expect, actual)


def test_straight_flush():
    """
    Testing a straight flush hand
    """

    hand = PokerHand([Card(8, "S"), Card(7, "S"), Card(6, "S"), Card(5, "S"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 4
    assert_equals("Getting rank of straight flush", expect, actual)


def test_normal_flush():
    """
    Testing a normal flush hand
    """

    hand = PokerHand([Card(11, "S"), Card(7, "S"), Card(3, "S"), Card(5, "S"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 4
    assert_equals("Getting rank of normal flush", expect, actual)


def test_four_kind():
    """
    Testing a four of a kind hand
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(11, "D"), Card(11, "C"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 3
    assert_equals("Getting rank of four-of-a-kind", expect, actual)


def test_full_house():
    """
    Testing a full house hand
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(11, "D"), Card(4, "C"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 3
    assert_equals("Getting rank of full house", expect, actual)


def test_two_pair():
    """
    Testing a two pair hand
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(7, "D"), Card(4, "C"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 3
    assert_equals("Getting rank of two pair", expect, actual)


def test_three_kind():
    """
    Testing a three-of-a-kind hand
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(11, "D"), Card(5, "C"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 2
    assert_equals("Getting rank of three-of-a-kind", expect, actual)


def test_pair():
    """
    Testing a pair hand
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(9, "D"), Card(5, "C"), Card(4, "S")])
    actual = hand.get_hand_ranking()
    expect = 2
    assert_equals("Getting rank of pair", expect, actual)


def test_straight():
    """
    Testing a straight hand
    """

    hand = PokerHand([Card(11, "S"), Card(10, "H"), Card(9, "D"), Card(8, "C"), Card(7, "S")])
    actual = hand.get_hand_ranking()
    expect = 1
    assert_equals("Getting rank of straight", expect, actual)


def test_high_card():
    """
    Testing a high_card hand
    """

    hand = PokerHand([Card(11, "S"), Card(5, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    actual = hand.get_hand_ranking()
    expect = 1
    assert_equals("Getting rank of pair", expect, actual)


def test_get_hand_ranking():
    """ 
    all get_hand_ranking tests
    """
    start_tests("get_hand_ranking testing")
    test_royal_flush()
    test_straight_flush()
    test_normal_flush()
    test_four_kind()
    test_full_house()
    test_two_pair()
    test_three_kind()
    test_pair()
    test_straight()
    test_high_card()
    finish_tests()


""" get_rank_count method unit tests start below """


def test_5_rank_hand():
    """
    Testing a hand with 5 cards all different ranks
    """

    hand = PokerHand([Card(11, "S"), Card(5, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    actual = hand.get_rank_count()
    expect = {11: 1, 5: 1, 9: 1, 2: 1, 7: 1}
    assert_equals("Getting count of 5 cards all different ranks", expect, actual)


def test_4_rank_hand():
    """
    Testing a hand with 5 cards including 1 duplicate rank
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    actual = hand.get_rank_count()
    expect = {11: 2, 9: 1, 2: 1, 7: 1}
    assert_equals("Getting count of 5 cards including 1 duplicate rank", expect, actual)


def test_3_rank_hand():
    """
    Testing a hand with 5 cards including 2 duplicate ranks
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(9, "D"), Card(9, "C"), Card(7, "S")])
    actual = hand.get_rank_count()
    expect = {11: 2, 9: 2, 7: 1}
    assert_equals("Getting count of 5 cards including 2 duplicate ranks", expect, actual)


def test_2_rank_hand():
    """
    Testing a hand with 5 cards including only 2 ranks
    """

    hand = PokerHand([Card(11, "S"), Card(11, "H"), Card(11, "D"), Card(9, "C"), Card(11, "C")])
    actual = hand.get_rank_count()
    expect = {11: 4, 9: 1}
    assert_equals("Getting count of 5 cards including only 2 ranks", expect, actual)


def test_get_rank_count():
    """ 
    all get_rank_count tests
    """
    start_tests("get_rank_count testing")
    test_5_rank_hand()
    test_4_rank_hand()
    test_3_rank_hand()
    test_2_rank_hand()
    finish_tests()


""" get_max_rank method unit tests start below """


def test_same_count():
    """
    Testing on count with 5 values
    """

    hand = PokerHand([Card(11, "S"), Card(5, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    count = {9: 1, 5: 1, 11: 1, 2: 1, 7: 1}
    actual = hand.get_max_rank(count)
    expect = 11
    assert_equals("Getting max rank of 5 count hand", expect, actual)


def test_max_value_lower_count():
    """
    Testing on count with the max value having a lesser count than another rank
    """

    hand = PokerHand([Card(2, "S"), Card(5, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    count = {9: 1, 5: 1, 2: 2, 7: 1}
    actual = hand.get_max_rank(count)
    expect = 2
    assert_equals("Getting max rank of count max value having a lesser count than another rank", expect, actual)


def test_max_value_higher_count():
    """
    Testing on count with the max value having the highest count
    """

    hand = PokerHand([Card(2, "S"), Card(9, "H"), Card(9, "D"), Card(2, "C"), Card(7, "S")])
    count = {9: 2, 2: 2, 7: 1}
    actual = hand.get_max_rank(count)
    expect = 9
    assert_equals("Getting max rank of count max value having a lesser count than another rank", expect, actual)


def test_get_max_rank():
    """ 
    all get_max_rank tests
    """
    start_tests("get_max_rank testing")
    test_same_count()
    test_max_value_lower_count()
    test_max_value_higher_count()
    finish_tests()


if __name__ == "__main__":
    test_compare_to()
    test_get_hand_ranking()
    test_get_rank_count()
    test_get_max_rank()
