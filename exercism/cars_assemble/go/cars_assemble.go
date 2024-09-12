package cars

const (
	CarGroupCoast  = 95000
	CarSingleCoast = 10000
)

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(
	productionRate int,
	successRate float64,
) float64 {
	return (float64(productionRate) * successRate) / float64(100)
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(
	productionRate int,
	successRate float64,
) int {
	result := (float64(productionRate) * (successRate / 100)) / 60
	return int(result)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	return (uint(carsCount)/10)*CarGroupCoast + (uint(carsCount)%10)*CarSingleCoast
}
