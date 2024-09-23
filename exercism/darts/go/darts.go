package darts

import "math"

func Score(x, y float64) int {
	centerToPoint := math.Sqrt(math.Pow(0-x, 2) + math.Pow(0-y, 2))
	switch {
	case centerToPoint <= 1:
		return 10
	case centerToPoint > 1 && centerToPoint <= 5:
		return 5
	case centerToPoint > 5 && centerToPoint <= 10:
		return 1
	default:
		return 0
		
	}
}
