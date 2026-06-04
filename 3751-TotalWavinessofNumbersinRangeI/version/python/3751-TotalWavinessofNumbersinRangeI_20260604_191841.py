# Last updated: 6/4/2026, 7:18:41 PM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        def waviness(x):
4            s = str(x)
5            n = len(s)
6
7            if n < 3:
8                return 0
9
10            cnt = 0
11
12            for i in range(1, n - 1):
13                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1]):
14                    cnt += 1
15
16            return cnt
17
18        ans = 0
19
20        for x in range(num1, num2 + 1):
21            ans += waviness(x)
22
23        return ans