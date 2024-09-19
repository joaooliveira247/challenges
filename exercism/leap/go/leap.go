package leap

// IsLeapYear return true if year is leap else false.
func IsLeapYear(year int) bool {
	if val := year % 100; val != 0 {
		return val%4 == 0
	} else {
		return year%400 == 0
	}
}
