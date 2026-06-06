# Last updated: 6/6/2026, 8:09:48 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        result = [0 for _ in range(len(nums))]
4        total = sum(nums)
5        left = 0
6
7        for i in range(len(nums)):
8            total -= nums[i]
9            result[i] = abs(total - left)
10            left += nums[i]
11        
12        return result