# Last updated: 10/2/2026, 6:57:53 AM
1class Solution:
2    def searchRange(self, nums: list[int], target: int) -> list[int]:
3
4        def find_first():
5            left = 0
6            right = len(nums) - 1
7            answer = -1
8
9            while left <= right:
10                mid = (left + right) // 2
11
12                if nums[mid] == target:
13                    answer = mid
14                    right = mid - 1
15                elif nums[mid] < target:
16                    left = mid + 1
17                else:
18                    right = mid - 1
19
20            return answer
21
22        def find_last():
23            left = 0
24            right = len(nums) - 1
25            answer = -1
26
27            while left <= right:
28                mid = (left + right) // 2
29
30                if nums[mid] == target:
31                    answer = mid
32                    left = mid + 1
33                elif nums[mid] < target:
34                    left = mid + 1
35                else:
36                    right = mid - 1
37
38            return answer
39
40        return [find_first(), find_last()]