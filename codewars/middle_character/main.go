package main

import "fmt"

func GetMiddle(s string) string {
	if len(s) == 1 {
		return s
	}

	if length := len(s); length%2 == 0 {
		return s[(length/2)-1 : (length/2)+1]
	} else {
		return string(s[(length/2)])
	}

}

func main() {
	testCases := []string{"test", "testing", "middle", "A"}

	for _, testCase := range testCases {
		fmt.Println(GetMiddle(testCase))
	}
}
