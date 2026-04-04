package main

import "fmt"

func Add(n int) func(int) int {
	return func(i int) int { return i + n }
}

func main() {
	fmt.Println(Add(1)(3))
	fmt.Println(Add(1)(21))

}
