package booking

import (
	"fmt"
	"time"
)

func parseDateByLayout(layout string, date string) time.Time {
	t, _ := time.Parse(layout, date)
	return t
}

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {
	layout := "1/2/2006 15:04:05"
	return parseDateByLayout(layout, date)
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	layout := "January 2, 2006 15:04:05"
	dateParsed := parseDateByLayout(layout, date)
	return dateParsed.Before(time.Now())
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	layout := "Monday, January 2, 2006 15:04:05"
	dateParsed := parseDateByLayout(layout, date)
	if hour := dateParsed.Hour(); hour >= 12 && hour < 18 {
		return true
	}
	if dateParsed.Year() < time.Now().Year() {
		return false
	}
	return false
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	dateParsed := Schedule(date)
	return fmt.Sprintf(
		"You have an appointment on %s, %s %d, %d, at %d:%d.",
		dateParsed.Weekday(),
		dateParsed.Month(),
		dateParsed.Day(),
		dateParsed.Year(),
		dateParsed.Hour(),
		dateParsed.Minute(),
	)
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	t := time.Date(time.Now().Year(), time.September, 15, 0, 0, 0, 0, time.UTC)
	return t
}
