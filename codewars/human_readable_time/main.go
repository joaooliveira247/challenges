package main

import (
	"fmt"
	"strings"
)

func formatTime(time int) string {
	if time/10 < 1 {
		return fmt.Sprintf("0%d", time)
	}
	return fmt.Sprintf("%d", time)
}

func HumanReadableTime(seconds int) string {
	var time strings.Builder

	timeConst := 3600

	for idx := 0; idx < 3; idx++ {

		if idx == 2 {
			fmt.Fprintf(&time, "%s", formatTime(seconds/timeConst))
			continue
		}

		fmt.Fprintf(&time, "%s:", formatTime(seconds/timeConst))
		seconds = seconds % timeConst
		timeConst = timeConst / 60
	}

	return time.String()
}

func main() {
	fmt.Println(HumanReadableTime(59))
}
