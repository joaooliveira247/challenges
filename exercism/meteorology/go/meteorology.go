package meteorology

import "fmt"

type TemperatureUnit int

const (
	Celsius    TemperatureUnit = 0
	Fahrenheit TemperatureUnit = 1
)

// Add a String method to the TemperatureUnit type
func (temp TemperatureUnit) String() string {
	units := []string{"°C", "°F"}
	return units[temp]
}

type Temperature struct {
	degree int
	unit   TemperatureUnit
}

// Add a String method to the Temperature type
func (temp Temperature) String() string {
	return fmt.Sprintf("%d %s", temp.degree, temp.unit.String())
}

type SpeedUnit int

const (
	KmPerHour    SpeedUnit = 0
	MilesPerHour SpeedUnit = 1
)

// Add a String method to SpeedUnit
func (temp SpeedUnit) String() string {
	units := []string{"km/h", "mph"}
	return units[temp]
}

type Speed struct {
	magnitude int
	unit      SpeedUnit
}

func (vel Speed) String() string {
	return fmt.Sprintf("%d %s", vel.magnitude, vel.unit.String())
}

// Add a String method to Speed

type MeteorologyData struct {
	location      string
	temperature   Temperature
	windDirection string
	windSpeed     Speed
	humidity      int
}

// Add a String method to MeteorologyData
func (metData MeteorologyData) String() string {
	//San Francisco: 57 °F, Wind NW at 19 mph, 60% Humidity
	return fmt.Sprintf(
		"%s: %s, Wind %s at %s, %d%% Humidity",
		metData.location,
		metData.temperature.String(),
		metData.windDirection,
		metData.windSpeed.String(),
		metData.humidity,
	)
}
