# Last updated: 7/22/2026, 6:26:03 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        left_max = right_max = 0
5        water = 0
6
7        while left < right:
8            if height[left] < height[right]:
9                if height[left] >= left_max:
10                    left_max = height[left]
11                else:
12                    water += left_max - height[left]
13                left += 1
14            else:
15                if height[right] >= right_max:
16                    right_max = height[right]
17                else:
18                    water += right_max - height[right]
19                right -= 1
20
21        return water