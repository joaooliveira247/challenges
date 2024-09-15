package airportrobot

import "fmt"

// Write your code here.
// This exercise does not have tests for each individual task.
// Try to solve all the tasks first before running the tests.
type Greeter interface {
	LanguageName() string
	Greet(visitorsName string) string
}

type Italian struct{}

type Portuguese struct{}

func SayHello(name string, greeter Greeter) string {
	return fmt.Sprintf(
		"I can speak %s: %s",
		greeter.LanguageName(),
		greeter.Greet(name),
	)
}

func (nationality Italian) LanguageName() string {
	return "Italian"
}

func (nationality Italian) Greet(visitorsName string) string {
	return fmt.Sprintf("Ciao %s!", visitorsName)
}

func (nationality Portuguese) LanguageName() string {
	return "Portuguese"
}

func (nationality Portuguese) Greet(visitorsName string) string {
	return fmt.Sprintf("Olá %s!", visitorsName)
}
