# Last updated: 9/10/2026, 11:15:37 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        self.count = 0
10        def dfs(node):
11            if not node:
12                return 0, 0
13
14            left_sum, left_count = dfs(node.left)
15            right_sum, right_count = dfs(node.right)
16
17            total_sum = left_sum + right_sum + node.val
18            total_count = left_count + right_count + 1
19
20            if total_sum // total_count == node.val:
21                self.count += 1
22
23            return total_sum, total_count
24
25        dfs(root)
26        return self.count