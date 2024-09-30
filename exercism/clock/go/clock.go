package clock

import (
	"time"
)

// Define the Clock type here.
type Clock struct {
	Hour, Minute int
}

func genTime(h, m int) time.Time {
	clock := time.Time{}
	clock = clock.Add(
		time.Hour*time.Duration(h) + time.Minute*time.Duration(m),
	)
	return clock
}

func New(h, m int) Clock {
	clock := genTime(h, m)
	return Clock{Hour: clock.Hour(), Minute: clock.Minute()}
}

func (c Clock) Add(m int) Clock {
	clock := genTime(c.Hour, c.Minute)
	clock = clock.Add(time.Minute * time.Duration(m))
	c.Hour = clock.Hour()
	c.Minute = clock.Minute()
	return c
}

func (c Clock) Subtract(m int) Clock {
	clock := genTime(c.Hour, c.Minute)
	clock = clock.Add(time.Duration(-m) * time.Minute)
	c.Hour = clock.Hour()
	c.Minute = clock.Minute()
	return c
}

func (c Clock) String() string {
	clock := genTime(c.Hour, c.Minute)
	return clock.Format("15:04")
}
