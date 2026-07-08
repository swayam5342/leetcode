# Last updated: 7/8/2026, 11:42:32 PM
1from bisect import bisect_left, bisect_right
2class Solution:
3    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
4        MOD = 10 ** 9 + 7
5        pos = []
6        digits = []
7
8        for i, ch in enumerate(s):
9            if ch != '0':
10                pos.append(i)
11                digits.append(int(ch))
12
13        m = len(digits)
14        pow10 = [1] * (m + 1)
15        for i in range(1, m + 1):
16            pow10[i] = (pow10[i - 1] * 10) % MOD
17
18        prefSum = [0] * (m + 1)
19        poly = [0] * (m + 1)
20
21        for i in range(m):
22            prefSum[i + 1] = prefSum[i] + digits[i]
23            poly[i + 1] = (poly[i] * 10 + digits[i]) % MOD
24
25        ans = []
26
27        for l, r in queries:
28            L = bisect_left(pos, l)
29            R = bisect_right(pos, r) - 1
30
31            if L > R:
32                ans.append(0)
33                continue
34
35            k = R - L + 1
36
37            digit_sum = prefSum[R + 1] - prefSum[L]
38
39            x = (poly[R + 1] - poly[L] * pow10[k]) % MOD
40
41            ans.append((x * digit_sum) % MOD)
42
43        return ans