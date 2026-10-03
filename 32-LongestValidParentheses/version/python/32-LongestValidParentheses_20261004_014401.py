# Last updated: 10/4/2026, 1:44:01 AM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        ans = 0
5
6        for i, ch in enumerate(s):
7            if ch == '(':
8                stack.append(i)
9            else:
10                stack.pop()
11
12                if not stack:
13                    stack.append(i)
14                else:
15                    ans = max(ans, i - stack[-1])
16
17        return ans