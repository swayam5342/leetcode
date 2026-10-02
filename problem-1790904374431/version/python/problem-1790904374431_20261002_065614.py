# Last updated: 10/2/2026, 6:56:14 AM
1class Solution:
2    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
3        n = len(matrix)
4
5        left = matrix[0][0]
6        right = matrix[n - 1][n - 1]
7
8        while left < right:
9            mid = (left + right) // 2
10
11            count = 0
12            row = n - 1
13            col = 0
14            while row >= 0 and col < n:
15                if matrix[row][col] <= mid:
16                    count += row + 1
17                    col += 1
18                else:
19                    row -= 1
20
21            if count < k:
22                left = mid + 1
23            else:
24                right = mid
25
26        return left