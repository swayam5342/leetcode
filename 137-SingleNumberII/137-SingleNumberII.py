# Last updated: 3/22/2026, 2:33:11 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        ones = 0
4        twos = 0
5        
6        for num in nums:
7            ones = (ones ^ num) & ~twos
8            twos = (twos ^ num) & ~ones
9        
10        return ones