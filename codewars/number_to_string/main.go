package main

import "fmt"

func NumberToString(n int) string {
	return fmt.Sprintf("%d", n)
}

func main() {
	fmt.Println(NumberToString(123))
	fmt.Println(NumberToString(999))
	fmt.Println(NumberToString(-777))
}
