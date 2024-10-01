// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package triangle should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package triangle

// Notice KindFromSides() returns this type. Pick a suitable data type.
type Kind int

const (
	// Pick values for the following identifiers used by the test program.
	NaT Kind = iota // not a triangle
	Equ             // equilateral
	Iso             // isosceles
	Sca             // scalene
)

// KindFromSides should have a comment documenting it.
func KindFromSides(a, b, c float64) Kind {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers may protest!
	if !(a+b > c) || !(b+c > a) || !(a+c > b) {
		return NaT

	}
	sides := []float64{a, b, c}
	combs := [][]int{
		{0, 1}, {1, 2}, {2, 0},
	}
	var l []bool
	for _, index := range combs {
		if result := sides[index[0]] == sides[index[1]]; result {
			l = append(l, result)
		}
	}
	var k Kind
	switch len(l) {
	case 3:
		k = Equ
	case 2, 1:
		k = Iso
	default:
		k = Sca
	}
	return k
}
