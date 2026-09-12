# Last updated: 9/12/2026, 2:48:19 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = set()
4        while n != 1:
5            if n in seen:
6                return False
7
8            seen.add(n)
9
10            total = 0
11            while n > 0:
12                digit = n % 10
13                total += digit * digit
14                n //= 10
15
16            n = total
17
18        return True