# Last updated: 7/22/2026, 6:39:56 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        m=len(nums)
4        s=sum(nums)
5        s1=m*(m+1)//2
6        return s1-s