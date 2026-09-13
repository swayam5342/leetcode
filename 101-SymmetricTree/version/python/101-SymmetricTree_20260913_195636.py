# Last updated: 9/13/2026, 7:56:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def mirror(left, right):
10            if not left and not right:
11                return True
12
13            if not left or not right:
14                return False
15
16            return (left.val == right.val and
17                    mirror(left.left, right.right) and
18                    mirror(left.right, right.left))
19
20        return mirror(root.left, root.right)