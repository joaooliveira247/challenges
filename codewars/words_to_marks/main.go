package main

import "fmt"

func WordsToMarks(s string) (total int) {
    for _, char := range s {
    	total += int(char - 96)
    }
    
    return total
}

func main() {
	fmt.Println(WordsToMarks("attitude"))
}