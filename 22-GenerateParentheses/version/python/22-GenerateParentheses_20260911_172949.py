# Last updated: 9/11/2026, 5:29:49 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        result = []
4
5        def backtrack(s, open_count, close_count):
6            if len(s) == 2 * n:
7                result.append(s)
8                return
9
10            if open_count < n:
11                backtrack(s + "(", open_count + 1, close_count)
12
13            if close_count < open_count:
14                backtrack(s + ")", open_count, close_count + 1)
15
16        backtrack("", 0, 0)
17        return result