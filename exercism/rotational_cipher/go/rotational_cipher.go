package rotationalcipher

import "unicode"

func upperLetter(l rune, key int) rune {
	// A - Z (65 - 90) 25
	newLetter := l + rune(key)
	if newLetter > 90 {
		return 65 + (newLetter - 91)
	}
	return newLetter
}

func lowerLetter(l rune, key int) rune {
	// a - z (97 - 122) 25 | A - Z (65 - 90) 25
	if !(l > 96 && l < 123) {
		return l
	}
	newLetter := l + rune(key)
	if newLetter > 122 {
		return 97 + (newLetter - 123)
	}
	return newLetter
}

func RotationalCipher(plain string, shiftKey int) string {
	// a - z (97 - 122) 25 | A - Z (65 - 90) 25
	encryptedText := []rune{}
	text := []rune(plain)
	for _, letter := range text {
		if unicode.IsUpper(letter) {
			encryptedText = append(
				encryptedText,
				upperLetter(letter, shiftKey),
			)
			continue
		}
		encryptedText = append(encryptedText, lowerLetter(letter, shiftKey))
	}
	return string(encryptedText)
}
