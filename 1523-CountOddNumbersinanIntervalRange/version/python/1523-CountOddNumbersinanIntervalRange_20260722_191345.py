# Last updated: 7/22/2026, 7:13:45 PM
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        if low%2==0 and high%2==0:
4            return (-low+high) // 2
5        else:
6            return (high-low)//2 +1