# Last updated: 9/14/2026, 10:50:19 AM
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        return (rec1[0] < rec2[2] and
4                rec2[0] < rec1[2] and
5                rec1[1] < rec2[3] and
6                rec2[1] < rec1[3])