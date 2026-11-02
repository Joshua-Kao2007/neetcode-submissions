class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while i < index and cur:
            cur = cur.next
            i += 1
        return cur.val if i == index and cur else -1

    def addAtHead(self, val: int) -> None:
        cur_next = self.head.next
        new_node = ListNode(val)
        self.head.next = new_node
        new_node.next = cur_next

    def addAtTail(self, val: int) -> None:
        cur,prv = self.head.next, self.head
        while cur:
            prv = cur
            cur = cur.next
        prv.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        cur,prv = self.head.next, self.head
        while i < index and cur:
            i += 1
            prv = cur
            cur = cur.next
        if i==index:
            new_node = ListNode(val)
            prv.next = new_node
            new_node.next = cur

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        cur,prv = self.head.next, self.head
        while i < index and cur and cur.next:
            i += 1
            prv = cur
            cur = cur.next
        if i==index and cur:
            next_node = cur.next
            cur.next = None
            prv.next = next_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)