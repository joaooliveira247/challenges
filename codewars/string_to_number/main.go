package main

import "fmt"

func tenPow(n int) int {
	if n == 0 {
		return 1
	}
	return 10 * tenPow(n-1)
}

func StringToNumber(str string) int {
	var total int
	var hasSignal bool

	if str[0] == '-' {
		str = str[1:]
		hasSignal = true
	}

	mult := tenPow(len(str) - 1)

	for _, val := range str {
		total += int(val-48) * mult
		mult /= 10
	}

	if hasSignal {
		return total * -1
	}
	return total
}

func main() {
	fmt.Println(StringToNumber("1234"))
	fmt.Println(StringToNumber("605"))
	fmt.Println(StringToNumber("1405"))
	fmt.Println(StringToNumber("-7"))
}
