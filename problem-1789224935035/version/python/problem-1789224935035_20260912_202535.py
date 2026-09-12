# Last updated: 9/12/2026, 8:25:35 PM
1
2
3class Solution:
4    def minDays(self, n: int) -> int:
5        k = 1
6        while (k+1)*(k+2) //2 <= n:
7            k +=1
8        inf = float('inf')
9        dp = [inf]*(n+1)
10        dp[0]=0
11
12        for i in range(1,n+1):
13            for j in range(1,k+1):
14                t = j*(j+1)//2
15                if t > i:
16                    break
17                if dp[i-t] + (j+1) < dp[i]:
18                    dp[i] = dp[i-t] + (j+1)
19
20        return dp[n] - 1
21        