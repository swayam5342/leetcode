# Last updated: 6/15/2026, 1:19:36 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return None
10
11        slow = head
12        fast = head
13        prev = None
14
15        while fast and fast.next:
16            prev = slow
17            slow = slow.next
18            fast = fast.next.next
19
20        prev.next = slow.next
21
22        return head