package main

import "fmt"

func finalValueAfterOperations(operations []string) int {
	x := 0
	for _, value := range operations {
		switch value {
		case "++X", "X++":
			x++
		case "--X", "X--":
			x--
		}

	}
	return x
}

func main() {
	opr := []string{"--X", "X++", "X++"}
	fmt.Println(finalValueAfterOperation(opr))
}
