# Last updated: 9/8/2026, 11:10:51 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        ans = 0
4        if n >= 1000:
5            ans += n - 999
6
7        if n > 100000:
8            ans += n - 99999
9
10        return ans
11        