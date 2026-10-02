# Last updated: 10/2/2026, 7:35:24 AM
1class Solution:
2    def increasingTriplet(self, nums: list[int]) -> bool:
3        first = float('inf')
4        second = float('inf')
5
6        for num in nums:
7            if num <= first:
8                first = num
9
10            elif num <= second:
11                second = num
12
13            else:
14                return True
15
16        return False