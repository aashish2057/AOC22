package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("input1-1.txt")
	check(err)
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	var max int
	for i := 0; i < len(lines); i++ {
		sum := 0
		for i < len(lines) && lines[i] != "" {
			val, err := strconv.Atoi(lines[i])
			check(err)
			sum += val
			i += 1
			fmt.Println(sum, max)
		}
		if max < sum {
			max = sum
		}
	}
	fmt.Print(max)

}
