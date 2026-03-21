# Last updated: 3/22/2026, 12:45:52 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, '032b')[::-1], 2)