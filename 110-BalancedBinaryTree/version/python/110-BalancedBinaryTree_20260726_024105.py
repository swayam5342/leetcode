# Last updated: 7/26/2026, 2:41:05 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def height(node):
10            if not node:
11                return 0
12
13            left = height(node.left)
14            if left == -1:
15                return -1
16
17            right = height(node.right)
18            if right == -1:
19                return -1
20
21            if abs(left - right) > 1:
22                return -1
23
24            return 1 + max(left, right)
25
26        return height(root) != -1