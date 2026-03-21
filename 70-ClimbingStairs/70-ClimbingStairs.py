# Last updated: 3/22/2026, 12:45:59 AM
class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        if n in memo:
            return memo[n]
        
        if n==1:
            return 1
        if n==2:
            return 2
        x = self.climbStairs(n-1)+ self.climbStairs(n-2)
        memo[n] = x
        return x