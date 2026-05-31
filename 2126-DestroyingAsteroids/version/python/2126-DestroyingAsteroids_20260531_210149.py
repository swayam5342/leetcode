# Last updated: 5/31/2026, 9:01:49 PM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4        m = mass
5        for i in asteroids:
6            if m >= i:
7                m+=i
8            else:
9                return False
10        
11        return True