# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# decomposition into its littlest parts and detail oriented
class Solution:
    def linkedListToNumber(self, l1: Optional[ListNode]) -> int:
        cur = l1
        cur_num = 0
        cur_tens = 1

        while cur:
            cur_val = cur.val
            cur_num += cur_tens * cur_val
            cur_tens *= 10 
            cur = cur.next

        return cur_num

    def numberToLinkedList(self, num: int)-> Optional[ListNode]:
        cur = num
        cur_node = dummy = ListNode(-1)
        if num < 10:
            cur_node.next = ListNode(num)
            return cur_node.next

        while cur > 0:
            next_node = ListNode(cur%10)
            cur_node.next = next_node
            cur_node = cur_node.next
            cur //= 10

        return dummy.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.linkedListToNumber(l1)
        num2 = self.linkedListToNumber(l2)
        num3 = num1+num2
        return self.numberToLinkedList(num3)
        
        # reverse_function 1 li1
        # reverse function 2 li2
        # simple addition
        # reverse function 2 back to linked list and return root




        # reverse_function 1 (Linked LIst) --> Number 
        # reverse_function 2 (number --> Linked List)