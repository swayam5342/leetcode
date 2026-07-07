# Last updated: 7/7/2026, 10:43:27 PM
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        s = ''
4        k = 0
5        for i in str(n):
6            if i == '0':
7                ...
8            else:
9                s += i
10                k += int(i)
11        if not s:
12            s = 0
13        return k * int(s)