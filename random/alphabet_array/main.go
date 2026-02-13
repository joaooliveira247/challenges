package main

import "fmt"

func alphabet_array(n uint) []string {
	var array []string

	if n > 27 {
		n = n % 27
	}

	for i := rune(65); i < 91 && i < 65+rune(n); i++ {
		array = append(array, string(i))
	}

	return array
}

/*
This challenge consist of:

Give a number 'n', return an array with 'n' alphabet letters.
*/
func main() {
	result := alphabet_array(27)

	fmt.Println(result)
}
