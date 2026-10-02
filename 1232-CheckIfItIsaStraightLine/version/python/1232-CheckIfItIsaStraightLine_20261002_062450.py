# Last updated: 10/2/2026, 6:24:50 AM
1class Solution:
2    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
3        x1, y1 = coordinates[0]
4        x2, y2 = coordinates[1]
5
6        dx = x2 - x1
7        dy = y2 - y1
8
9        for i in range(2, len(coordinates)):
10            x, y = coordinates[i]
11
12            if (x - x1) * dy != (y - y1) * dx:
13                return False
14
15        return True