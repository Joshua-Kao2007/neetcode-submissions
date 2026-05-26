class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def get(self, index:int) -> int: # get the value at index; if the index is invalid, return -1
        if index >= self.size:
            return -1
        cur = self.head.next
        for i in range(0, index):
            cur = cur.next
        return cur.val 

    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val)
        tmp = self.head.next
        self.head.next = new_node
        tmp.prev = new_node
        new_node.prev = self.head
        new_node.next = tmp
        self.size += 1
    
    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val)
        tmp = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.prev = tmp
        new_node.next = self.tail
        self.size += 1
    
    def addAtIndex(self, index:int, val:int) -> None:
        if index > self.size:
            return
        cur = self.head.next
        for i in range(0, index):
            cur = cur.next
        new_node = ListNode(val)
        prv = cur.prev
        cur.prev = new_node
        prv.next = new_node
        new_node.prev = prv
        new_node.next = cur
        self.size += 1
            
    def deleteAtIndex(self, index:int) -> None:
        if index >= self.size:
            return
        cur = self.head.next
        for i in range(0, index):
            cur = cur.next
        prv = cur.prev
        nxt = cur.next
        prv.next = nxt
        nxt.prev = prv
        self.size -= 1

# l1 = MyLinkedList()
# l1.addAtHead(1)
# l1.addAtTail(3)
# l1.addAtIndex(1,2)
# print(l1.get(1))
# l1.deleteAtIndex(1)
# print(l1.get(1))