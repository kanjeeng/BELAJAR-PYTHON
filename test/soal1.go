package main

import (
	"fmt"
	"math"
)

func main() {
	var R, r, t, t1 int
	var LS, ls, lp float64
	fmt.Scan(&R, &r, &t, &t1)
	hitungLuasSelimut_1303223064(r, t1, &ls)
	hitungLuasSelimut_1303223064(R, t, &LS)
	lp = luasAlas_1303223064(R) + luasAlas_1303223064(r) + LS - ls

	fmt.Println(LS)
	fmt.Println(ls)
	fmt.Println(lp)
}
func luasAlas_1303223064(r int) float64 {
	return float64(r) * float64(r) * 3.14
}
func garisPelukis_1303223064(r, t int) float64 {
	return math.Sqrt(float64(r*r) + float64(t*t))
}
func hitungLuasSelimut_1303223064(r int, t int, luas *float64) {
	var s float64
	s = garisPelukis_1303223064(r, t)
	*luas = 3.14 * float64(r) * s
}
