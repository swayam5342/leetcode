# Last updated: 3/22/2026, 2:44:43 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        si = -1 if x < 0 else 1
4        r = 0
5        x = abs(x)
6        while x !=0:
7            d = x %10
8            x = x//10
9            if r > (2**31 -1)//10:
10                return 0
11            r = r*10 + d
12        return r * si
13        