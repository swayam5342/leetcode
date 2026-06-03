# Last updated: 6/3/2026, 7:35:15 PM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        minLandFinish = min(
4            s + d for s, d in zip(landStartTime, landDuration)
5        )
6
7        ans = float('inf')
8
9        for s, d in zip(waterStartTime, waterDuration):
10            ans = min(ans, max(minLandFinish, s) + d)
11
12        minWaterFinish = min(
13            s + d for s, d in zip(waterStartTime, waterDuration)
14        )
15
16        for s, d in zip(landStartTime, landDuration):
17            ans = min(ans, max(minWaterFinish, s) + d)
18
19        return ans