# Last updated: 5/29/2026, 4:43:25 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        s_to_t = {}
4        t_to_s = {}
5
6        for a, b in zip(s, t):
7            if a in s_to_t and s_to_t[a] != b:
8                return False
9
10            if b in t_to_s and t_to_s[b] != a:
11                return False
12
13            s_to_t[a] = b
14            t_to_s[b] = a
15
16        return True