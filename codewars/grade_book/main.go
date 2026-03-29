package main

import "fmt"

func GetGrade(a, b, c int) rune {
	avg := (a + b + c) / 3

	switch {
	case avg >= 90:
		return 'A'
	case avg < 90 && avg >= 80:
		return 'B'
	case avg < 80 && avg >= 70:
		return 'C'
	case avg < 70 && avg >= 60:
		return 'D'
	default:
		return 'F'
	}
}

func main() {
	fmt.Println(string(GetGrade(70, 70, 70)))
}
