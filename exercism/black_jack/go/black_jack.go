package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "ten", "king", "jack", "queen":
		return 10
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	sum_cards := ParseCard(card1) + ParseCard(card2)

	switch {
	case sum_cards == 22:
		return "P"
	case sum_cards == 21:
		switch dealerCard {
		case "ace", "ten", "king", "queen", "jack":
			return "S"
		default:
			return "W"
		}
	case sum_cards >= 17 && sum_cards <= 20:
		return "S"
	case sum_cards >= 12 && sum_cards <= 16:
		switch {
		case ParseCard(dealerCard) >= 7:
			return "H"
		default:
			return "S"
		}
	default:
		return "H"
	}
}
