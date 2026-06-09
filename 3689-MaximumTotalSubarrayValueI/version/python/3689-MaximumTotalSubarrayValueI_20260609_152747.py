# Last updated: 6/9/2026, 3:27:47 PM
1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        return (max(nums)-min(nums))*k