# Last updated: 10/2/2026, 6:37:09 AM
1class Solution:
2    def flipLights(self, n: int, presses: int) -> int:
3
4        if presses == 0:
5            return 1
6
7        if n == 1:
8            return 2
9
10        if n == 2:
11            if presses == 1:
12                return 3
13            return 4
14
15        # n >= 3
16        if presses == 1:
17            return 4
18        if presses == 2:
19            return 7
20        return 8