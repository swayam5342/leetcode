# Last updated: 10/2/2026, 7:57:08 AM
1class Solution:
2    def computeArea(
3        self,
4        ax1: int, ay1: int, ax2: int, ay2: int,
5        bx1: int, by1: int, bx2: int, by2: int
6    ) -> int:
7        area1 = (ax2 - ax1) * (ay2 - ay1)
8        area2 = (bx2 - bx1) * (by2 - by1)
9        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
10        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
11
12        overlap = overlap_width * overlap_height
13
14        return area1 + area2 - overlap