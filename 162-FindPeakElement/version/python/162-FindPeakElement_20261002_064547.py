# Last updated: 10/2/2026, 6:45:47 AM
1class Solution:
2    def findPeakElement(self, nums: list[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if nums[mid] < nums[mid + 1]:
10                left = mid + 1
11            else:
12                right = mid
13
14        return left