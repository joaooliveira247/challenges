package partyrobot

import (
	"fmt"
	"strings"
)

// rjust take a string and fill right with given character
func rjust(s string, width uint, fillchar string) string {
	return fmt.Sprintf("%s%s", strings.Repeat(fillchar, int(width)-len(s)), s)
}

// Welcome greets a person by name.
func Welcome(name string) string {
	return fmt.Sprintf("Welcome to my party, %s!", name)
}

// HappyBirthday wishes happy birthday to the birthday person and exclaims their age.
func HappyBirthday(name string, age int) string {
	return fmt.Sprintf(
		"Happy birthday %s! You are now %d years old!",
		name,
		age,
	)
}

// AssignTable assigns a table to each guest.
func AssignTable(
	name string,
	table int,
	neighbor, direction string,
	distance float64,
) string {
	return fmt.Sprintf(
		"Welcome to my party, %s!\nYou have been assigned to table %s. Your table is %s, exactly %.1f meters from here.\nYou will be sitting next to %s.",
		name,
		rjust(fmt.Sprintf("%d", table), 3, "0"),
		direction,
		distance,
		neighbor,
	)
}
