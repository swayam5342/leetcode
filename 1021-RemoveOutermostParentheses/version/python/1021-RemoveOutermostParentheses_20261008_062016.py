# Last updated: 10/8/2026, 6:20:16 AM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        result = []
4        depth = 0
5
6        for ch in s:
7            if ch == '(':
8                if depth > 0:
9                    result.append(ch)
10                depth += 1
11
12            else:
13                depth -= 1
14                if depth > 0:
15                    result.append(ch)
16
17        return ''.join(result)