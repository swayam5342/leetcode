# Last updated: 10/2/2026, 6:39:58 AM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        current = nums[0]
4        maximum = nums[0]
5
6        for i in range(1, len(nums)):
7            current = max(nums[i], current + nums[i])
8            maximum = max(maximum, current)
9
10        return maximum