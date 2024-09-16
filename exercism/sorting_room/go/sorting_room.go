package sorting

import (
	"fmt"
	"strconv"
)

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	return fmt.Sprintf("This is the number %.1f", f)
}

type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {
	return fmt.Sprintf(
		"This is a box containing the number %.1f",
		float64(nb.Number()),
	)
}

type FancyNumber struct {
	n string
}

func (i FancyNumber) Value() string {
	return i.n
}

type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {
	switch fnb.(type) {
	case FancyNumber:
		value, _ := strconv.Atoi(fnb.Value())
		return value
	default:
		return 0
	}
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {
	value := ExtractFancyNumber(fnb)
	return fmt.Sprintf(
		"This is a fancy box containing the number %.1f",
		float64(value),
	)
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i interface{}) string {
	var msg string
	switch value := i.(type) {
	case int:
		msg = DescribeNumber(float64(value))
	case float64:
		msg = DescribeNumber(value)
	case NumberBox:
		msg = DescribeNumberBox(value)
	case FancyNumberBox:
		msg = DescribeFancyNumberBox(value)
	default:
		msg = "Return to sender"
	}
	return msg
}
