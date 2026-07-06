# Last updated: 7/6/2026, 11:57:41 PM
1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[0], -x[1]))
4
5        count = 0
6        max_right = -1
7
8        for left, right in intervals:
9            if right > max_right:
10                count += 1
11                max_right = right
12
13        return count