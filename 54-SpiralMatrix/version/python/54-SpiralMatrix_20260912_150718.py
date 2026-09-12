# Last updated: 9/12/2026, 3:07:18 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        ans = []
4        top = 0
5        bottom = len(matrix) - 1
6        left = 0
7        right = len(matrix[0]) - 1
8
9        while top <= bottom and left <= right:
10
11            for i in range(left, right + 1):
12                ans.append(matrix[top][i])
13            top += 1
14
15            for i in range(top, bottom + 1):
16                ans.append(matrix[i][right])
17            right -= 1
18
19            if top <= bottom:
20                for i in range(right, left - 1, -1):
21                    ans.append(matrix[bottom][i])
22                bottom -= 1
23
24            if left <= right:
25                for i in range(bottom, top - 1, -1):
26                    ans.append(matrix[i][left])
27                left += 1
28
29        return ans