# Last updated: 9/11/2026, 5:53:34 AM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        count = [0] * 10
4        for d in digits:
5            count[d] += 1
6
7        ans = 0
8
9        for num in range(100, 1000):
10            if num % 2 != 0:
11                continue
12
13            a = num // 100
14            b = (num // 10) % 10
15            c = num % 10
16
17            need = [0] * 10
18            need[a] += 1
19            need[b] += 1
20            need[c] += 1
21
22            possible = True
23
24            for d in range(10):
25                if need[d] > count[d]:
26                    possible = False
27                    break
28
29            if possible:
30                ans += 1
31
32        return ans