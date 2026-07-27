# Last updated: 7/27/2026, 10:43:44 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        nums.sort()
4        return (nums[-1]-1)*(nums[-2]-1)