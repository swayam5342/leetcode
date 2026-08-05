# Last updated: 8/5/2026, 4:41:35 PM
1class Solution:
2    def trailingZeroes(self, n: int) -> int:
3        count = 0
4        while n >0:
5            count += n//5
6            n =n//5
7        return count