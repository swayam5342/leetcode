# Last updated: 10/2/2026, 6:03:18 AM
1class Solution:
2    def rangeBitwiseAnd(self, left: int, right: int) -> int:
3        shift = 0
4
5        while left != right:
6            left >>= 1
7            right >>= 1
8            shift += 1
9
10        return left << shift