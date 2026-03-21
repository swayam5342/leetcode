# Last updated: 3/22/2026, 12:45:43 AM
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n ==0:
            return 1
        l = len(bin (n)) - 2
        k = (1 << l)-1
        return n ^ k
        