# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # two approaches
        #1 Array brute force approach O(N), O(N)
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        L,R = 0, len(arr)-1
        while L <= R:
            if L == R:
                arr[L].next = None
                break
            arr[L].next = arr[R]

            if L+1 == R:
                arr[R].next = None
                break
            arr[R].next = arr[L+1]
            L, R = L+1, R-1

        return