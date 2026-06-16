# Last updated: 6/16/2026, 12:38:27 PM
1class Solution:
2    def processStr(self, s: str) -> str:
3        r = []
4
5        for ch in s:
6            if ch == "#":
7                r.extend(r)
8            elif ch == "*":
9                if r:
10                    r.pop()
11            elif ch == "%":
12                r.reverse()
13            else:
14                r.append(ch)
15        return "".join(r)