# Last updated: 5/30/2026, 8:18:38 PM
1class Solution:
2    def isPowerOfFour(self, n: int) -> bool:
3        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0