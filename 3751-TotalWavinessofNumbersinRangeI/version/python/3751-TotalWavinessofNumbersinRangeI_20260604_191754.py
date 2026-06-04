# Last updated: 6/4/2026, 7:17:54 PM
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
13                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or \
14                   (s[i] < s[i - 1] and s[i] < s[i + 1]):
15                    cnt += 1
16
17            return cnt
18
19        ans = 0
20
21        for x in range(num1, num2 + 1):
22            ans += waviness(x)
23
24        return ans