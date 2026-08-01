# Last updated: 8/1/2026, 9:44:33 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6
7        ans = 1
8
9        while n > 0:
10            if n % 2 == 1:
11                ans *= x
12            x *= x
13            n //= 2
14
15        return ans