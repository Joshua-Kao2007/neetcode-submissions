# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = p3 = ListNode(-1)
        p1,p2 = list1,list2
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = ListNode(p1.val)
                p1 = p1.next
            else:
                cur.next = ListNode(p2.val)
                p2 = p2.next
            cur = cur.next
        cur.next = p1 if p1 else p2
        return p3.next