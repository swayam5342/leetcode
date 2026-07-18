# Last updated: 7/18/2026, 3:37:18 PM
1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n <= 0:
4            return False
5
6        for factor in [2, 3, 5]:
7            while n % factor == 0:
8                n //= factor
9
10        return n == 1
11        