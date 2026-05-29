# Last updated: 5/29/2026, 1:09:20 PM
1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        return min(sum(int(d) for d in str(x)) for x in nums)