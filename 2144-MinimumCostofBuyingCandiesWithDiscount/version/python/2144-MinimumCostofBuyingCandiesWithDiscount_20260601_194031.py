# Last updated: 6/1/2026, 7:40:31 PM
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse=True)
4
5        total = 0
6
7        for i in range(len(cost)):
8            if i % 3 != 2:
9                total += cost[i]
10
11        return total