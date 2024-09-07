"""Functions for tracking poker hands and assorted card tasks.

Python list documentation:
https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number + x for x in range(3)]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds_1.extend(rounds_2)

    return rounds_1


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR
    ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the
    `true average`?
    """

    avg: float = card_average(hand)
    avg_first_last: float = sum([hand[0], hand[-1]]) / 2

    if avg == avg_first_last:
        return True
    elif len(hand) % 2 == 1:
        return avg == float(hand[len(hand) // 2])
    else:
        return False


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) ==
    (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    odd: list[int] = hand[::2]
    even: list[int] = list(set(hand).difference(odd))

    return card_average(odd) == card_average(even)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[len(hand) - 1] == 11:
        hand[len(hand) - 1] = 22
    return hand
