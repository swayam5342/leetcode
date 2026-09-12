# Last updated: 9/12/2026, 2:57:53 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        words = s.split()
4
5        if len(pattern) != len(words):
6            return False
7
8        p_to_w = {}
9        w_to_p = {}
10
11        for p, w in zip(pattern, words):
12            if p in p_to_w and p_to_w[p] != w:
13                return False
14
15            if w in w_to_p and w_to_p[w] != p:
16                return False
17
18            p_to_w[p] = w
19            w_to_p[w] = p
20
21        return True