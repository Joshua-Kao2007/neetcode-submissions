# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1: O(N) O(N) using hash map with indicies to values going that way
        if not head or not head.next:return 
        map = {}
        cur = head
        cnt = 0
        while cur:
            map[cnt] = cur
            cur = cur.next
            cnt += 1
#[2,4,6,8] --> map[0]=listnode(2) --> map[1]=listnode(4) --> map[2]=listnode(6)-->map[3]=listnode(8)
        cur = head
        for i in range(1,cnt): # till 4
            if i%2 == 0:
                cnter = i//2
            else:
                cnter = cnt-((i+1)//2)
            cur.next = map[cnter]
            cur = cur.next
        cur.next = None