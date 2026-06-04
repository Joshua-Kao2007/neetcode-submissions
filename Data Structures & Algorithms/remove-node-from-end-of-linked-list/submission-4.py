# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        print(prev.val)
        dummy = ListNode(-1)
        dummy.next = prev
        cur = dummy
        for i in range(n-1):
            cur = cur.next
        cur.next = cur.next.next
        # dummy --> 4-->3-->2-->1-->None

        # reverse back
        cur = dummy.next
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev