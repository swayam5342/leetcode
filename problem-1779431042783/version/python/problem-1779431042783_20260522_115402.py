# Last updated: 5/22/2026, 11:54:02 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        for i in range(len(nums)):
4            if nums[i] == target:
5                return i
6        else:
7            return -1