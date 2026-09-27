# Last updated: 9/27/2026, 9:09:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
9        if not nums:
10            return None
11
12        mid = len(nums) // 2
13
14        root = TreeNode(nums[mid])
15
16        root.left = self.sortedArrayToBST(nums[:mid])
17        root.right = self.sortedArrayToBST(nums[mid + 1:])
18
19        return root