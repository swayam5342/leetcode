# Last updated: 10/4/2026, 3:33:27 AM
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        i = len(num1) - 1
4        j = len(num2) - 1
5        carry = 0
6        result = []
7
8        while i >= 0 or j >= 0 or carry:
9            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
10            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
11
12            total = digit1 + digit2 + carry
13
14            result.append(str(total % 10))
15            carry = total // 10
16
17            i -= 1
18            j -= 1
19
20        return ''.join(reversed(result))