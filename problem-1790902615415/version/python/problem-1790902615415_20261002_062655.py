# Last updated: 10/2/2026, 6:26:55 AM
1class Solution:
2    def hammingDistance(self, x: int, y: int) -> int:
3        n = x ^ y
4        count = 0
5        while n:
6            count += n & 1
7            n >>= 1
8
9        return count