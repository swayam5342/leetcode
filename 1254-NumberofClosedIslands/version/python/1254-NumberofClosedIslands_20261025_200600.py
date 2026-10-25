# Last updated: 10/25/2026, 8:06:00 PM
1from typing import List
2
3class Solution:
4    def closedIsland(self, grid: List[List[int]]) -> int:
5        m, n = len(grid), len(grid[0])
6
7        def sink(r, c):
8            stack = [(r, c)]
9            grid[r][c] = 1
10            while stack:
11                i, j = stack.pop()
12                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
13                    x, y = i + di, j + dj
14                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
15                        grid[x][y] = 1
16                        stack.append((x, y))
17
18        for i in range(m):
19            for j in range(n):
20                if (i in (0, m-1) or j in (0, n-1)) and grid[i][j] == 0:
21                    sink(i, j)
22
23
24        count = 0
25    
26        for i in range(1, m-1):
27            for j in range(1, n-1):
28                if grid[i][j] == 0:
29                    count += 1
30                    sink(i, j)
31        return count