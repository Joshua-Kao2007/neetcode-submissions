class ListNode:
    def __init__(self, val, nextt = None, prev = None):
        self.val = val
        self.prev = prev
        self.nextt = nextt
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.nextt, self.tail.prev = self.tail, self.head

    def get(self, index:int) -> int: # get the value at index; if the index is invalid, return -1
        cur,cnt = self.head.nextt,0
        while cur.nextt and cnt < index:
            cur = cur.nextt
            cnt += 1
        return cur.val if cnt == index else -1
        
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val)
        tmp = self.head.nextt
        self.head.nextt, tmp.prev = new_node, new_node
        new_node.prev, new_node.nextt = self.head, tmp
    
    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val)
        tmp = self.tail.prev
        self.tail.prev.nextt, self.tail.prev = new_node, new_node
        new_node.prev, new_node.nextt = tmp, self.tail
    
    def addAtIndex(self, index:int, val:int) -> None:
        # first get to that index, then insert the value...if end then insert at end...else nothing gets inserted
        cur,cnt = self.head.nextt,0
        while cur.nextt and cnt < index:
            cur = cur.nextt
            cnt += 1
        if cur and cnt == index:
            new_node = ListNode(val)
            prv = cur.prev
            cur.prev, prv.nextt = new_node, new_node
            new_node.prev, new_node.nextt = prv, cur
    def deleteAtIndex(self, index:int) -> None:
        cur,cnt = self.head.nextt,0
        while cur.nextt and cnt < index:
            cur = cur.nextt
            cnt += 1
        if cur.nextt and cnt == index:
            prv,nxt = cur.prev, cur.nextt
            prv.nextt, nxt.prev = nxt, prv

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)