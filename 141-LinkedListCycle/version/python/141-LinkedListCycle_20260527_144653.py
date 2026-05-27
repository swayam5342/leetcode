# Last updated: 5/27/2026, 2:46:53 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        n = head
10        nn = head
11        while nn and nn.next:
12            n= n.next
13            nn= nn.next.next
14            if n == nn:
15                return True
16        
17        return False