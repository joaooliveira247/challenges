"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    special_cards: dict[str, int] = {"J": 10, "Q": 10, "K": 10, "A": 1}

    if card.isnumeric() and (int(card) > 1 and int(card) <= 10):
        return int(card)
    return special_cards[card]


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of
    equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value_one: int = value_of_card(card_one)
    value_two: int = value_of_card(card_two)

    if value_one == value_two:
        return card_one, card_two
    elif value_one > value_two:
        return card_one
    else:
        return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    hand: list[str] = [card_one, card_two]

    if "A" in hand:
        return 1

    hand_value: int = value_of_card(card_one) + value_of_card(card_two)

    if hand_value > 10:
        return 1
    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    real_bj_cards: list[str] = ["10", "J", "Q", "K"]

    hand: list[str] = [card_one, card_two]

    if "A" in hand:
        hand.remove("A")
        if hand[0] in real_bj_cards:
            return True
        return False
    return False


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs?
    (i.e. cards are of the same value).
    """
    special_cards: set[str] = {"Q", "K"}

    if card_one == card_two:
        return True
    if special_cards.issubset({card_one, card_two}):
        return True
    return False


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down?
    (i.e. totals 9, 10 or 11 points).
    """

    hand: int = value_of_card(card_one) + value_of_card(card_two)

    if card_one == "A" and card_two == "A":
        return False
    elif hand < 12:
        return True
    else:
        return False
