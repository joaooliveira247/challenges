package main

import "fmt"

func Solution(str string) []string {
	switch len(str) {
	case 2:
		return []string{str}
	case 1:
		return []string{str + "_"}
	}
	
	return append([]string{str[:2]}, Solution(str[2:])...)
}

func main() {
	fmt.Println(Solution("abc"))
	fmt.Println(Solution("abcdef"))
}
