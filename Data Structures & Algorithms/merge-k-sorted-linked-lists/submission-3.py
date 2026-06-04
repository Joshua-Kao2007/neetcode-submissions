# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:    
    def merge(self,l1,l2) -> Optional[ListNode]:
        # TWo pointers
        l3 = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val: 
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1: l3.next = l1
        if l2: l3.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:return None
        while len(lists)>1:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(self.merge(l1,l2))
        
        return lists.pop()