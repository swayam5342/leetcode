# Last updated: 8/31/2026, 7:15:07 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        prev = head
9        curr = head.next
10        position = 1
11
12        first_critical = -1
13        prev_critical = -1
14        min_distance = float("inf")
15        while curr and curr.next:
16            is_critical = (
17                (curr.val > prev.val and curr.val > curr.next.val) or
18                (curr.val < prev.val and curr.val < curr.next.val)
19            )
20
21            if is_critical:
22                if first_critical == -1:
23                    first_critical = position
24                else:
25                    min_distance = min(
26                        min_distance,
27                        position - prev_critical
28                    )
29
30                prev_critical = position
31
32            prev = curr
33            curr = curr.next
34            position += 1
35        if first_critical == -1 or first_critical == prev_critical:
36            return [-1, -1]
37
38        max_distance = prev_critical - first_critical
39
40        return [min_distance, max_distance]