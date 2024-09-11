// Package weather_forecast provides tools to info about weather.
package weather

// CurrentCondition represents a certain weather condition.
var CurrentCondition string

// CurrentLocation represents a determinate location in the world.
var CurrentLocation string

// Forecast returns a string value equal to CurrentLocation plus CurrentCondition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
