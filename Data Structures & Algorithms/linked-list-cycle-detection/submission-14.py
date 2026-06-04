# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slowly linked lists
        if not head:return False
        fast_pointer = head.next
        slow_pointer = head
        while slow_pointer:
            if fast_pointer == slow_pointer: return True
            if fast_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
            else:
                return False

            slow_pointer = slow_pointer.next
    
        return False