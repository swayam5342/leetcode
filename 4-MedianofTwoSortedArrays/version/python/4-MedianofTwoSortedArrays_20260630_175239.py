# Last updated: 6/30/2026, 5:52:39 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        if len(nums1) > len(nums2):
4            nums1, nums2 = nums2, nums1
5
6        m, n = len(nums1), len(nums2)
7
8        low, high = 0, m
9
10        while low <= high:
11            partition1 = (low + high) // 2
12            partition2 = (m + n + 1) // 2 - partition1
13            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
14            right1 = float('inf') if partition1 == m else nums1[partition1]
15
16            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
17            right2 = float('inf') if partition2 == n else nums2[partition2]
18            if left1 <= right2 and left2 <= right1:
19                if (m + n) % 2 == 1:
20                    return max(left1, left2)
21                return (max(left1, left2) + min(right1, right2)) / 2
22            elif left1 > right2:
23                high = partition1 - 1
24            else:
25                low = partition1 + 1