# Last updated: 7/10/2026, 9:05:52 PM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
3        arr = sorted((v, i) for i, v in enumerate(nums))
4
5        values = [x[0] for x in arr]
6        idx = [x[1] for x in arr]
7        rank = [0] * n
8        for i, node in enumerate(idx):
9            rank[node] = i
10        comp = [0] * n
11        cid = 0
12        for i in range(1, n):
13            if values[i] - values[i - 1] > maxDiff:
14                cid += 1
15            comp[i] = cid
16        far = [0] * n
17        j = 0
18        for i in range(n):
19            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
20                j += 1
21            far[i] = j
22
23        LOG = (n).bit_length()
24
25        up = [far]
26        for _ in range(1, LOG):
27            prev = up[-1]
28            cur = [0] * n
29            for i in range(n):
30                cur[i] = prev[prev[i]]
31            up.append(cur)
32
33        ans = []
34
35        for u, v in queries:
36            if u == v:
37                ans.append(0)
38                continue
39
40            ru = rank[u]
41            rv = rank[v]
42
43            if ru > rv:
44                ru, rv = rv, ru
45
46            if comp[ru] != comp[rv]:
47                ans.append(-1)
48                continue
49
50            pos = ru
51            jumps = 0
52
53            for k in range(LOG - 1, -1, -1):
54                nxt = up[k][pos]
55                if nxt < rv:
56                    pos = nxt
57                    jumps += 1 << k
58
59            ans.append(jumps + 1)
60
61        return ans