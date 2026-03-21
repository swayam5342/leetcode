# Last updated: 3/22/2026, 2:41:58 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        sign = 0
4        n = ''
5        for i in str(x):
6            if i == '-':
7                sign = 1
8            else:
9                n = i + n
10        if(sign):
11            n = (0-int(n))
12        else:
13            n= int(n)
14        if(n > 2**31 or n < (-2**31 - 1)):
15            return 0
16        return n
17        