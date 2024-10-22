package cipher

import (
	"strings"
)

// Define the shift and vigenere types here.
type shift struct {
	distance int
}
type vigenere struct {
	key string
}
type caesar struct {
	shift int
}

// Both types should satisfy the Cipher interface.
func cleanString(s string) string {
	var newString strings.Builder
	s = strings.ToLower(s)

	for _, letter := range s {
		if letter > 96 && letter < 123 {
			newString.WriteRune(letter)
		}
	}
	return newString.String()
}

func eval(key string, length int) []int {
	length -= len(key)
	newKey := key
	for length > 0 {
		if length/len(key) > 0 {
			newKey = newKey + key
		} else {
			newKey = newKey + string(key[:length])
		}
		length -= len(key) // 6 // 2
	}

	var evaluate []int

	for _, letter := range newKey {
		evaluate = append(evaluate, int(letter)-97)
	}

	return evaluate
}

func NewCaesar() Cipher {
	return caesar{3}
}

func (c caesar) Encode(input string) string {
	input = cleanString(input)
	var newString strings.Builder
	for _, letter := range input {
		newLetter := letter + rune(c.shift)
		if newLetter > 122 {
			newLetter = rune(96) + newLetter - rune(122)
		}
		newString.WriteRune(newLetter)
	}
	return newString.String()
}

func (c caesar) Decode(input string) string {
	var newString strings.Builder
	for _, letter := range input {
		newLetter := letter - rune(c.shift)
		if newLetter < 97 {
			newLetter = rune(122) - (rune(96) - newLetter)
		}
		newString.WriteRune(newLetter)
	}
	return newString.String()
}

func NewShift(distance int) Cipher {
	if (distance >= 1 && distance <= 25) || (distance <= -1 && distance >= -25) {
		return shift{distance: distance}
	}
	// If the distance is invalid (e.g., 0 or out of bounds), return nil
	return nil
}

func (c shift) Encode(input string) string {
	input = cleanString(input)
	var newString strings.Builder
	for _, letter := range input {
		newLetter := letter + rune(c.distance)
		if newLetter > 122 {
			newLetter = rune(96) + newLetter - rune(122)
		} else if newLetter < 97 {
			newLetter = rune(122) - (rune(96) - newLetter)
		}
		newString.WriteRune(newLetter)
	}
	return newString.String()
}

func (c shift) Decode(input string) string {
	var newString strings.Builder
	for _, letter := range input {
		newLetter := letter - rune(c.distance)
		if newLetter < 97 {
			newLetter = rune(122) - (rune(96) - newLetter)
		} else if newLetter > 122 {
			newLetter = rune(96) + (newLetter - rune(122))
		}
		newString.WriteRune(newLetter)
	}
	return newString.String()
}

func NewVigenere(key string) Cipher {
	if len(strings.Split(key, " ")) > 1 || len(key) == 0 || len(key) == strings.Count(key, "a") {
		return nil
	}

	for _, letter := range key {
		if letter < 97 || letter > 122 {
			return nil
		}
	}

	return vigenere{key: key}
}

func (v vigenere) Encode(input string) string {
	input = cleanString(input)

	eval := eval(v.key, len(input)) 

	var newString strings.Builder

	for i := 0; i < len(input); i++ {
		shift := eval[i] 
		char := input[i]

		newLetter := char + byte(shift)
		if newLetter > 'z' { 
			newLetter = 'a' + (newLetter - 'z' - 1)
		}
		newString.WriteByte(newLetter)
	}

	return newString.String()
}

func (v vigenere) Decode(input string) string {
	input = cleanString(input)

	eval := eval(v.key, len(input))

	var newString strings.Builder

	for i := 0; i < len(input); i++ {
		shift := eval[i] 
		char := input[i]

		newLetter := char - byte(shift)
		if newLetter < 'a' {
			newLetter = 'z' - ('a' - newLetter - 1)
		}
		newString.WriteByte(newLetter)
	}

	return newString.String()
}
