# Last updated: 9/12/2026, 6:45:25 PM
1class Solution:
2    def grayCode(self, n: int) -> List[int]:
3        return [i ^ (i >> 1) for i in range(1 << n)]