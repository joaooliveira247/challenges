package main

import "fmt"

func GetCount(str string) (count int) {	
	for _, char := range str {
		switch char {
			case 'a', 'e', 'i', 'o', 'u':
				count++
		}
	}
	
	return count
}

func main() {
	fmt.Println(GetCount("abracadabra"))
}