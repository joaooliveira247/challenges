package main

import "fmt"

type IntList []int

func (s IntList) Foldl(fn func(int, int) int, initial int) int {
	agg := initial

	if s.Length() == 0 {
		return initial
	}

	for _, val := range s {
		agg = fn(agg, val)
	}

	return agg
}

func (s IntList) Foldr(fn func(int, int) int, initial int) int {
	if s.Length() == 0 {
		return initial
	}

	agg := initial

	for i := s.Length() - 1; i >= 0; i-- {
		agg = fn(s[i], agg)
	}

	return agg
}

func (s IntList) Filter(fn func(int) bool) IntList {
	newArray := IntList{}

	for _, val := range s {
		if fn(val) {
			newArray = append(newArray, val)
		}
	}

	return newArray
}

func (s IntList) Length() int {
	agg := 0
	for range s {
		agg++
	}
	return agg
}

func (s IntList) Map(fn func(int) int) IntList {
	for idx, val := range s {
		s[idx] = fn(val)
	}

	return s
}

func (s IntList) Reverse() IntList {
	newList := IntList{}

	for i := s.Length() - 1; i >= 0; i-- {
		newList = append(newList, s[i])
	}

	return newList
}

func (s IntList) Append(lst IntList) IntList {
	for _, val := range lst {
		s = append(s, val)
	}

	return s
}

func (s IntList) Concat(lists []IntList) IntList {
	for _, list := range lists {
		s = s.Append(list)
	}

	return s
}

func main() {

	l1 := IntList{1, 2, 3, 4, 5, 6, 7, 8}
	l2 := IntList{9, 10, 11}
	l3 := IntList{12, 13}
	l4 := []IntList{l2, l3}

	fmt.Println("Length", l1.Length())
	fmt.Println("Reverse", l1.Reverse())
	fmt.Println("Append", l1.Append(l2))
	fmt.Println("Concat", l1.Concat(l4))
	fmt.Println("Map", l1.Map(func(i int) int { return i + 1 }))

}
