# Last updated: 10/24/2026, 8:39:44 AM
1class Solution:
2    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
3                          arriveBob: str, leaveBob: str) -> int:
4        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
5        prefix = [0]
6        for d in days:
7            prefix.append(prefix[-1] + d)
8
9        def to_day(s: str) -> int:
10            month, day = int(s[:2]), int(s[3:])
11            return prefix[month - 1] + day
12
13        start = max(to_day(arriveAlice), to_day(arriveBob))
14        end = min(to_day(leaveAlice), to_day(leaveBob))
15        return max(0, end - start + 1)