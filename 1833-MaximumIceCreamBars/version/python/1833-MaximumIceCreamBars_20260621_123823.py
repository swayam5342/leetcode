# Last updated: 6/21/2026, 12:38:23 PM
1class Solution:
2    def maxIceCream(self, costs: List[int], coins: int) -> int:
3        max_cost = max(costs)
4        freq = [0] * (max_cost + 1)
5
6        for cost in costs:
7            freq[cost] += 1
8
9        count = 0
10
11        for cost, f in enumerate(freq):
12            if cost == 0:
13                continue
14
15            if f * cost <= coins:
16                count += f
17                coins -= f * cost
18            else:
19                count += coins // cost
20                break
21
22        return count