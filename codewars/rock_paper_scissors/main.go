package main

import "fmt"

func Rps(p1, p2 string) string {
	if p1 == p2 {
		return "Draw!"
	}

	winnerCases := map[string]string{
		"rock":     "scissors",
		"scissors": "paper",
		"paper":    "rock",
	}

	if winnerCases[p1] == p2 {
		return "Player 1 won!"
	}
	return "Player 2 won!"
}

func main() {
	fmt.Println(Rps("scissors", "paper"))
	fmt.Println(Rps("scissors", "rock"))
	fmt.Println(Rps("paper", "paper"))
}
