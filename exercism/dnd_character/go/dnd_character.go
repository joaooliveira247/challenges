package dndcharacter

import (
	"math"
	"math/rand"
	"slices"
)

type Character struct {
	Strength     int
	Dexterity    int
	Constitution int
	Intelligence int
	Wisdom       int
	Charisma     int
	Hitpoints    int
}

func rowDice() int {
	return rand.Intn(5) + 1
}

// Modifier calculates the ability modifier for a given ability score
func Modifier(score int) int {
	opr := (float64(score - 10)) / 2
	if opr < 0 {
		return int(math.Round(opr))
	}
	return int(opr)
}

// Ability uses randomness to generate the score for an ability
func Ability() int {
	round := []int{}

	for i := 0; i < 4; i++ {
		round = append(round, rowDice())
	}
	slices.Sort(round)

	total := 0

	for _, value := range round[1:] {
		total += value
	}
	return total
}

// GenerateCharacter creates a new Character with random scores for abilities
func GenerateCharacter() Character {
	character := Character{
		Strength:     Ability(),
		Dexterity:    Ability(),
		Constitution: Ability(),
		Intelligence: Ability(),
		Wisdom:       Ability(),
		Charisma:     Ability(),
	}
	character.Hitpoints = (character.Constitution + 10) / 2
	return character
}
