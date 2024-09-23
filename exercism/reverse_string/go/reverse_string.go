package reverse

func Reverse(input string) string {
	runes := []rune(input)
	newString := []rune{}
	for i := len(runes) - 1; i >= 0; i-- {
		newString = append(newString, runes[i])
	}
	return string(newString)
}
