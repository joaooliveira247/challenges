package main

import (
	"fmt"
)

func reverseString(x string) string {
	var newString string
	for i := len(x) - 1; i >= 0; i-- {
		newString += string(x[i])
	}
	return newString
}

func isPalindrome(x int) bool {
	numString := fmt.Sprintf("%d", x)
	return numString == reverseString(numString)
}

func main() {
	fmt.Println(isPalindrome(121))
}
