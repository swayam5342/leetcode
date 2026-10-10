# Last updated: 10/10/2026, 8:41:06 PM
1from bisect import bisect_left,insort
2import sys
3class Solution:
4    def minInversions(self, words: list[str], target: list[int]) -> int:
5        sys.setrecursionlimit(10000)
6        n = len(words)
7        pos = [0] * n
8        for p,i in enumerate(target):
9            pos[i] = p
10
11        kids = [{}]
12        mark = [-1]
13
14        for idx,w in enumerate(words):
15            u = 0
16            for ch in w:
17                nxt = kids[u].get(ch)
18                if nxt is None:
19                    nxt = len(kids)
20                    kids[u][ch] = nxt
21                    kids.append({})
22                    mark.append(-1)
23                u = nxt
24            mark[u] = idx
25
26        total = 0
27        def cross(A,B):
28            c = j = 0
29            lb = len(B)
30            for x in A:
31                while j < lb and B[j] < x:
32                    j+=1
33                c +=j
34            return c
35
36        def dfs(u):
37            nonlocal total
38            lists = [dfs(v) for v in kids[u].values()]
39            k = len(lists)
40            if k >= 2:
41                w = [[0]*k for _ in range(k)]
42                for a in range(k):
43                    for b in range(a+1,k):
44                        c = cross(lists[a],lists[b])
45                        w[a][b] = c
46                        w[b][a] = len(lists[a])*len(lists[b]) -c
47
48                full = 1 << k
49                inc =[]
50                for b in range(k):
51                    arr = [0]* full
52                    wb = [w[a][b] for a in range(k)]
53                    for m in range(1,full):
54                        low = (m & -m).bit_length() - 1
55                        arr[m] = arr[m & (m-1)] + wb[low]
56                    inc.append(arr)
57                INF = float('inf')
58                dp = [INF]*full
59                dp[0] = 0
60                for m in range(full):
61                    cur = dp[m]
62                    if cur == INF:
63                        continue
64                    for b in range(k):
65                        if not m >> b &1:
66                            nm = m | 1 << b
67                            val = cur + inc[b][m]
68                            if val < dp[nm]:
69                                dp[nm]=val
70                total+= dp[full-1]
71            if k ==1:
72                merged = lists[0]
73            elif k ==0:
74                merged = []
75            else:
76                merged = sorted(x for l in lists for x in l)
77            if mark[u] >= 0:
78                v = pos[mark[u]]
79                total += bisect_left(merged,v)
80                insort(merged,v)
81            return merged
82        dfs(0)
83        return total