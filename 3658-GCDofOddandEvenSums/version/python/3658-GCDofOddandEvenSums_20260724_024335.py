# Last updated: 7/24/2026, 2:43:35 AM
1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        return gcd(n*n,n*(n+1))
4        