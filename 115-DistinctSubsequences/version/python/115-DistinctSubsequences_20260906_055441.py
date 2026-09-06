# Last updated: 9/6/2026, 5:54:41 AM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m, n = len(s), len(t)
4        dp = [0] * (n + 1)
5        dp[0] = 1
6
7        for i in range(m):
8            for j in range(n - 1, -1, -1):
9                if s[i] == t[j]:
10                    dp[j + 1] += dp[j]
11
12        return dp[n]