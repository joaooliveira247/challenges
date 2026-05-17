package main

import (
	"fmt"
	"time"
)

func UnluckyDays(year int) int {
	var days int

	current := time.Date(year, time.January, 13, 0, 0, 0, 0, time.UTC)

	for current.Year() == year {
		if current.Weekday() == time.Friday {
			days++
		}
		current = current.AddDate(0, 1, 0)
	}

	return days
}

func main() {
	fmt.Println(UnluckyDays(2015))
	fmt.Println(UnluckyDays(1986))
}
