# Last updated: 3/22/2026, 12:46:18 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l : list[int] = list(str(x))
        point2= len(l)-1
        point1 = 0
        while point1 < point2:
            if l[point1] == l[point2]:
                point2 -= 1
                point1 += 1
            else:
                return False
        return True
