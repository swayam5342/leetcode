# Last updated: 5/30/2026, 8:20:59 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        dp = [0] * (n + 1)
4
5        for i in range(1, n + 1):
6            dp[i] = dp[i >> 1] + (i & 1)
7
8        return dp