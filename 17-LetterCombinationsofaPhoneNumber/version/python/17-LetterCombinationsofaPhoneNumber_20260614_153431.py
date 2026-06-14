# Last updated: 6/14/2026, 3:34:31 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        data = {
4            '2':['a','b','c'],
5            '3':['d','e','f'],
6            '4':['g','h','i'],
7            '5':['j','k','l'],
8            '6':['m','n','o'],
9            '7':['p','q','r','s'],
10            '8':['t','u','v'],
11            '9':['w','x','y','z']
12        }
13        result = []
14        def backtrack(index, current):
15            if index == len(digits):
16                result.append(current)
17                return
18
19            for ch in data[digits[index]]:
20                backtrack(index + 1, current + ch)
21
22        backtrack(0, "")
23        return result