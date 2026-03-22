package main

import "fmt"

func CreatePhoneNumber(numbers [10]uint) string {

	anyNumbers := make([]any, len(numbers))

	for i, v := range numbers {
		anyNumbers[i] = v
	}

	return fmt.Sprintf("(%d%d%d) %d%d%d-%d%d%d%d", anyNumbers...)
}

func main() {
	fmt.Println(CreatePhoneNumber([10]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}))
}
