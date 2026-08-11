# Last updated: 8/11/2026, 8:24:16 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        total = nums[0]
4        for i in range(1, len(nums)):
5            if nums[i] == nums[i - 1] + 1:
6                total += nums[i]
7            else:
8                break
9        nums_set = set(nums)
10        while total in nums_set:
11            total += 1
12
13        return total