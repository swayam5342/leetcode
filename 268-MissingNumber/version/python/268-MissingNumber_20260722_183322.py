# Last updated: 7/22/2026, 6:33:22 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        if 0 not in nums:
4            return 0
5        m=max(nums)
6        s=sum(nums)
7        s1=m*(m+1)//2
8        if s1-s ==0:
9            return m+1
10        return s1-s