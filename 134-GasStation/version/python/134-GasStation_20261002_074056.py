# Last updated: 10/2/2026, 7:40:56 AM
1class Solution:
2    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
3        total = 0
4        tank = 0
5        start = 0
6
7        for i in range(len(gas)):
8            diff = gas[i] - cost[i]
9
10            total += diff
11            tank += diff
12
13            if tank < 0:
14                start = i + 1
15                tank = 0
16
17        if total >= 0:
18            return start
19
20        return -1