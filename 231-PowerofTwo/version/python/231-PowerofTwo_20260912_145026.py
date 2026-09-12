# Last updated: 9/12/2026, 2:50:26 PM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        return n > 0 and (n & (n - 1)) == 0