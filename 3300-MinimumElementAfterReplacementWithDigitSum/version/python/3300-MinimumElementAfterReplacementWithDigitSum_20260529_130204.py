# Last updated: 5/29/2026, 1:02:04 PM
1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        l = [sum([int(j) for j in str(i)]) for i in nums]
4        return min(l)