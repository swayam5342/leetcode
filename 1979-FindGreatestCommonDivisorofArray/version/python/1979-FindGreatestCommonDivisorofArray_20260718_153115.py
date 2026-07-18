# Last updated: 7/18/2026, 3:31:15 PM
1from math import gcd
2class Solution:
3    def findGCD(self, nums: List[int]) -> int:
4        return gcd(max(nums),min(nums))