package main

import "fmt"

func SetAlarm(employed, vacation bool) bool {
	if employed && !vacation {
		return true
	}
	return false
}

func main() {
	fmt.Println(SetAlarm(true, true))
	fmt.Println(SetAlarm(true, false))
	fmt.Println(SetAlarm(false, true))
}
