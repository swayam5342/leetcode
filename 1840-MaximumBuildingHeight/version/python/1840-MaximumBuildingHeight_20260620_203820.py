# Last updated: 6/20/2026, 8:38:20 PM
1class Solution:
2    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
3        r = restrictions
4        r.append([1, 0])
5        r.sort()
6
7        if r[-1][0] != n:
8            r.append([n, n - 1])
9
10        r.sort()
11        for i in range(1, len(r)):
12            dist = r[i][0] - r[i - 1][0]
13            r[i][1] = min(r[i][1], r[i - 1][1] + dist)
14        for i in range(len(r) - 2, -1, -1):
15            dist = r[i + 1][0] - r[i][0]
16            r[i][1] = min(r[i][1], r[i + 1][1] + dist)
17
18        ans = 0
19        for i in range(len(r) - 1):
20            x1, h1 = r[i]
21            x2, h2 = r[i + 1]
22
23            dist = x2 - x1
24            peak = (h1 + h2 + dist) // 2
25
26            ans = max(ans, peak)
27
28        return ans