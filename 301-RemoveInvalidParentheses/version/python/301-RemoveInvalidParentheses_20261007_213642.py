# Last updated: 10/7/2026, 9:36:42 PM
1from collections import deque
2
3class Solution:
4    def removeInvalidParentheses(self, s: str) -> list[str]:
5        def is_valid(string):
6            balance = 0
7
8            for ch in string:
9                if ch == '(':
10                    balance += 1
11                elif ch == ')':
12                    balance -= 1
13
14                    if balance < 0:
15                        return False
16
17            return balance == 0
18
19        queue = deque([s])
20        visited = {s}
21        result = []
22
23        while queue:
24            found_valid = False
25
26            for _ in range(len(queue)):
27                current = queue.popleft()
28
29                if is_valid(current):
30                    result.append(current)
31                    found_valid = True
32                if found_valid:
33                    continue
34
35                for i in range(len(current)):
36                    if current[i] not in '()':
37                        continue
38
39                    next_string = current[:i] + current[i + 1:]
40
41                    if next_string not in visited:
42                        visited.add(next_string)
43                        queue.append(next_string)
44
45            if found_valid:
46                return result
47
48        return [""]