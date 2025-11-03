package main

import "fmt"

func strStr(haystack string, needle string) int {

	for i := 0; i < (len(haystack)-len(needle))+1; i++ {
		if haystack[i:len(needle)+i] == needle {
			return i
		}
	}

	return -1
}

func main() {
	fmt.Println(strStr("sadbutsad", "sad"))
	fmt.Println(strStr("leetcode", "leeto"))
}
