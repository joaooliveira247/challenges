package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	totalBirds := 0
	for _, value := range birdsPerDay {
		totalBirds += value
	}
	return totalBirds
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	end := (week * 7)
	var start int
	if week == 1 {
		start = 0
	} else {
		start = end - 7
	}
	return TotalBirdCount(birdsPerDay[start:end])
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i, value := range birdsPerDay {
		if value <= 5 && i%2 == 0 {
			birdsPerDay[i] += 1
			continue
		}
	}
	return birdsPerDay
}
