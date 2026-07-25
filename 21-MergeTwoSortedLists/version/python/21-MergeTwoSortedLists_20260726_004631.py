# Last updated: 7/26/2026, 12:46:31 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        curr = dummy
10
11        while list1 and list2:
12            if list1.val < list2.val:
13                curr.next = list1
14                list1 = list1.next
15            else:
16                curr.next = list2
17                list2 = list2.next
18            curr = curr.next
19
20        curr.next = list1 if list1 else list2
21
22        return dummy.next