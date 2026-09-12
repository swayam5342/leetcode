# Last updated: 9/12/2026, 3:07:59 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k == 0:
9            return head
10
11        curr = head
12        length = 1
13
14        while curr.next:
15            curr = curr.next
16            length += 1
17
18        k %= length
19
20        if k == 0:
21            return head
22
23        curr.next = head
24
25        steps = length - k
26
27        for _ in range(steps):
28            curr = curr.next
29
30        new_head = curr.next
31        curr.next = None
32
33        return new_head  