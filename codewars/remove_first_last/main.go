package main

import "fmt"

func RemoveChar(word string) string {
	return word[1 : len(word)-1]
}

func main() {
	fmt.Println(RemoveChar("eloquent"))
	fmt.Println(RemoveChar("country"))
	fmt.Println(RemoveChar("xyz"))
	fmt.Println(RemoveChar("ab"))
	
}
