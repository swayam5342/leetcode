# Last updated: 10/2/2026, 6:34:25 AM
1class Solution:
2    def lemonadeChange(self, bills: list[int]) -> bool:
3        five = 0
4        ten = 0
5
6        for bill in bills:
7
8            if bill == 5:
9                five += 1
10
11            elif bill == 10:
12                if five == 0:
13                    return False
14
15                five -= 1
16                ten += 1
17
18            else:
19                if ten > 0 and five > 0:
20                    ten -= 1
21                    five -= 1
22
23                elif five >= 3:
24                    five -= 3
25
26                else:
27                    return False
28
29        return True