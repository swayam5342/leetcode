# Last updated: 10/5/2026, 5:15:12 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = 0
4        high = 0
5
6        for ch in s:
7            if ch == '(':
8                low += 1
9                high += 1
10
11            elif ch == ')':
12                low -= 1
13                high -= 1
14
15            else:
16                low -= 1
17                high += 1
18            if high < 0:
19                return False
20            low = max(low, 0)
21
22        return low == 0