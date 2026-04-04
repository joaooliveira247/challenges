package main

import "fmt"

func RepeatStr(repetitions int, value string) string {
	if repetitions == 0 {
		return ""
	}
	return value + RepeatStr(repetitions-1, value)
}

func main() {
	fmt.Println(RepeatStr(6, "I"))
	fmt.Println(RepeatStr(5, "Hello"))
}
