package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, World!")
	var a = TwoSum([]int{2, 7, 11, 15}, 9)
	fmt.Println(a)
}

func TwoSum(nums []int, target int) []int {
	var length int = len(nums) - 1
	for i := 0; i < length; i++ {
		for j := i + 1; j <= length; j++ {
			if nums[i]+nums[j] == target {
				var a = nums[i] + nums[j]
				fmt.Println("target number", a)
				return []int{i, j}

			}
		}
	}
	return []int{}
}
