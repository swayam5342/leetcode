# Last updated: 6/18/2026, 10:30:09 AM
1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        hour %= 12
4        angle = abs(60 * hour - 11 * minutes) / 2
5        return min(angle, 360 - angle)