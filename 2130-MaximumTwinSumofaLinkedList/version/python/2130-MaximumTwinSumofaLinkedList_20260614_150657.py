# Last updated: 6/14/2026, 3:06:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        slow = head
9        fast = head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14        prev = None
15        curr = slow
16
17        while curr:
18            nxt = curr.next
19            curr.next = prev
20            prev = curr
21            curr = nxt
22        ans = 0
23        first = head
24        second = prev
25
26        while second:
27            ans = max(ans, first.val + second.val)
28            first = first.next
29            second = second.next
30
31        return ans