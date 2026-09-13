# Last updated: 9/13/2026, 8:04:00 AM
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        ans = 0
5
6        for dr in range(-(n - 1), n):
7            for dc in range(-(n - 1), n):
8                overlap = 0
9
10                for i in range(n):
11                    for j in range(n):
12                        ni = i + dr
13                        nj = j + dc
14
15                        if 0 <= ni < n and 0 <= nj < n:
16                            if img1[i][j] == 1 and img2[ni][nj] == 1:
17                                overlap += 1
18
19                ans = max(ans, overlap)
20
21        return ans