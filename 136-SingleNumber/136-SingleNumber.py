# Last updated: 3/22/2026, 2:29:32 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        n = 0
4        for i in nums:
5            n = n ^ i
6        return n