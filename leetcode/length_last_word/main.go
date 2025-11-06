package main

import "fmt"

func lengthOfLastWord(s string) int {
	var counter int

	for i := len(s) - 1; i >= 0; i-- {
		if s[i] != ' ' {
			counter++
			continue
		}
		if s[i] == ' ' && counter > 0 {
			return counter
		}
	}
	return counter
}

func main() {
	fmt.Println(lengthOfLastWord("  Hello      World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
	fmt.Println(lengthOfLastWord("a"))
}
