# Last updated: 10/2/2026, 7:37:09 AM
1class Solution:
2    def findMinArrowShots(self, points: list[list[int]]) -> int:
3        points.sort(key=lambda x: x[1])
4
5        arrows = 1
6        arrow = points[0][1]
7
8        for start, end in points[1:]:
9            if start > arrow:
10                arrows += 1
11                arrow = end
12
13        return arrows