# Last updated: 10/26/2026, 8:35:40 AM
1class Solution:
2    def countIslands(self, grid: List[List[int]], k: int) -> int:
3        m, n = len(grid), len(grid[0])
4        count = 0
5        for i in range(m):
6            for j in range(n):
7                if grid[i][j] > 0:
8                    total = 0
9                    stack = [(i, j)]
10                    total += grid[i][j]
11                    grid[i][j] = 0
12                    while stack:
13                        r, c = stack.pop()
14                        for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
15                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
16                                total += grid[nr][nc]
17                                grid[nr][nc] = 0
18                                stack.append((nr, nc))
19                    if total % k == 0:
20                        count += 1
21        return count