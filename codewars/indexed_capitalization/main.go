package main

import "fmt"

func Capitalize(st string, arr []int) string {
	bString := []byte(st)

	for _, idx := range arr {
		if lenString := len(bString); idx < lenString {
			bString[idx] -= 32
			continue
		}
	}
	return string(bString)
}

func main() {
	fmt.Println(Capitalize("abcdef", []int{1, 2, 5}))
	fmt.Println(Capitalize("abcdef", []int{1, 2, 5, 100}))
}
