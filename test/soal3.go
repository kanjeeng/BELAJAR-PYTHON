package main

import "fmt"

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	display_1303223064(x, y)
}
func isFaktor_1303223064(num, x int) bool {
	return num%x == 0
}
func jumlahFaktor_1303223064(num int, total *int) {
	for i := 1; i < num; i++ {
		if isFaktor_1303223064(num, i) {
			*total += i
		}
	}
}
func perfect_1303223064(num int) bool {
	var total int
	jumlahFaktor_1303223064(num, &total)
	return num == total
}
func display_1303223064(x, y int) {
	fmt.Print("Barisan Perfect Number: ")
	for x <= y {
		if perfect_1303223064(x) {
			fmt.Print(x, " ")
		}
		x++
	}
}
