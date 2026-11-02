class ListNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class BrowserHistory:
    def __init__(self, homepage: str):
        self.dummy_head = ListNode(-1)
        self.dummy_tail = ListNode(-1)
        self.home = self.current_page = ListNode(homepage)
        self.dummy_head.next, self.dummy_tail.prev = self.home, self.home

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.current_page.next = new_node
        new_node.prev = self.current_page
        self.current_page = self.current_page.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.current_page.prev:
            steps -= 1
            self.current_page = self.current_page.prev
        return self.current_page.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current_page.next:
            steps -= 1
            self.current_page = self.current_page.next
        return self.current_page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)