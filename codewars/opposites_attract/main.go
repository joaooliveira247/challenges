package main

import "fmt"

func LoveFunc(flower1, flower2 int) bool {
	if (flower1%2 == 0 && flower2%2 != 0) || (flower2%2 == 0 && flower1%2 != 0) {
		return true
	}
	return false
}

func main() {
	fmt.Println(LoveFunc(1,4)) // true
	fmt.Println(LoveFunc(2,2)) // false
	fmt.Println(LoveFunc(0,1)) // true
	fmt.Println(LoveFunc(0,0)) // false
}
