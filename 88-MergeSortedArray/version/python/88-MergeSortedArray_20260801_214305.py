# Last updated: 8/1/2026, 9:43:05 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i = m - 1       
7        j = n - 1          
8        k = m + n - 1   
9
10        while i >= 0 and j >= 0:
11            if nums1[i] > nums2[j]:
12                nums1[k] = nums1[i]
13                i -= 1
14            else:
15                nums1[k] = nums2[j]
16                j -= 1
17            k -= 1
18        while j >= 0:
19            nums1[k] = nums2[j]
20            j -= 1
21            k -= 1