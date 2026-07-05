# Last updated: 7/6/2026, 12:00:59 AM
1class Solution:
2    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
3        MOD = 10**9 + 7
4        n = len(board)
5        score = [[-1] * n for _ in range(n)]
6        ways = [[0] * n for _ in range(n)]
7
8        score[0][0] = 0
9        ways[0][0] = 1
10
11        for i in range(n):
12            for j in range(n):
13                if board[i][j] == "X":
14                    continue
15
16                if i == 0 and j == 0:
17                    continue
18
19                best_score = -1
20                best_ways = 0
21
22                if i > 0 and score[i - 1][j] != -1:
23                    if score[i - 1][j] > best_score:
24                        best_score = score[i - 1][j]
25                        best_ways = ways[i - 1][j]
26                    elif score[i - 1][j] == best_score:
27                        best_ways = (best_ways + ways[i - 1][j]) % MOD
28
29                if j > 0 and score[i][j - 1] != -1:
30                    if score[i][j - 1] > best_score:
31                        best_score = score[i][j - 1]
32                        best_ways = ways[i][j - 1]
33                    elif score[i][j - 1] == best_score:
34                        best_ways = (best_ways + ways[i][j - 1]) % MOD
35
36                if i > 0 and j > 0 and score[i - 1][j - 1] != -1:
37                    if score[i - 1][j - 1] > best_score:
38                        best_score = score[i - 1][j - 1]
39                        best_ways = ways[i - 1][j - 1]
40                    elif score[i - 1][j - 1] == best_score:
41                        best_ways = (best_ways + ways[i - 1][j - 1]) % MOD
42
43                if best_score == -1:
44                    continue
45
46                value = 0
47                if board[i][j].isdigit():
48                    value = int(board[i][j])
49
50                score[i][j] = best_score + value
51                ways[i][j] = best_ways
52
53        if ways[n - 1][n - 1] == 0:
54            return [0, 0]
55
56        return [score[n - 1][n - 1], ways[n - 1][n - 1]]