# Last updated: 10/6/2026, 8:12:21 AM
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        open_count = 0
4        ans = 0
5
6        for ch in s:
7            if ch == '(':
8                open_count += 1
9            else:
10                if open_count > 0:
11                    open_count -= 1
12                else:
13                    ans += 1
14
15        return ans + open_count