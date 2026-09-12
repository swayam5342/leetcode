# Last updated: 9/12/2026, 8:26:06 AM
1from bisect import bisect_right
2class Solution:
3    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
4        n = len(intervals)
5
6        arr = sorted(
7            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
8            key=lambda x: (x[1], x[0], x[3])
9        )
10
11        ends = [x[1] for x in arr]
12
13        prev = []
14        for l, r, w, i in arr:
15            j = bisect_right(ends, l - 1) - 1
16            prev.append(j)
17
18        dp = [[0] * (n + 1) for _ in range(5)]
19        chosen = [[()] * (n + 1) for _ in range(5)]
20
21        for k in range(1, 5):
22            for i in range(1, n + 1):
23                skip_score = dp[k][i - 1]
24                skip_indices = chosen[k][i - 1]
25
26                p = prev[i - 1] + 1
27                take_score = dp[k - 1][p] + arr[i - 1][2]
28                take_indices = tuple(
29                    sorted(chosen[k - 1][p] + (arr[i - 1][3],))
30                )
31
32                if take_score > skip_score:
33                    dp[k][i] = take_score
34                    chosen[k][i] = take_indices
35                elif take_score < skip_score:
36                    dp[k][i] = skip_score
37                    chosen[k][i] = skip_indices
38                else:
39                    dp[k][i] = skip_score
40                    chosen[k][i] = min(take_indices, skip_indices)
41
42        return list(chosen[4][n])