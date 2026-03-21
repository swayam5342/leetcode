# Last updated: 3/22/2026, 12:46:01 AM
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right