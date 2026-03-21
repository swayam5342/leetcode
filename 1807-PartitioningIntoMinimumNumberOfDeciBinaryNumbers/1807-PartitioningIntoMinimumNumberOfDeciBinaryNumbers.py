# Last updated: 3/22/2026, 12:45:41 AM
class Solution:
    def minPartitions(self, n: str) -> int:
        m = "987654321"
        for i in m:
            if i in n:
                return int(i)

        