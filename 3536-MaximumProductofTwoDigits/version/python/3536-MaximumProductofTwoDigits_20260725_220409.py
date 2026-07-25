# Last updated: 7/25/2026, 10:04:09 PM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        digits = [int(d) for d in str(n)]
4        digits.sort(reverse=True)
5        return digits[0] * digits[1]