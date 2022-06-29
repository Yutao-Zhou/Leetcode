#### List ####
# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.stack = [homepage]
#         self.current = 0

#     def visit(self, url: str) -> None:
#         self.stack = self.stack[:self.current + 1]
#         self.stack.append(url)
#         self.current += 1

#     def back(self, steps: int) -> str:
#         self.current -= steps
#         if self.current < 0:
#             self.current = 0
#         return self.stack[self.current]

#     def forward(self, steps: int) -> str:
#         self.current += steps
#         if self.current >= len(self.stack):
#             self.current = len(self.stack) - 1
#         return self.stack[self.current]

#### Linked List ####
# class BrowserHistory:
#     class node:
#         def __init__(self, val, next = None, prev = None):
#             self.val = val
#             self.next = None
#             self.prev = None
#     def __init__(self, homepage: str):
#         self.currentNode = self.node(homepage)

#     def visit(self, url: str) -> None:
#         last = self.currentNode
#         if self.currentNode.next:
#             self.currentNode.next.prev = None
#         self.currentNode.next = self.node(url)
#         self.currentNode = self.currentNode.next
#         self.currentNode.prev = last

#     def back(self, steps: int) -> str:
#         while self.currentNode.prev and steps > 0:
#             self.currentNode = self.currentNode.prev
#             steps -= 1
#         return self.currentNode.val

#     def forward(self, steps: int) -> str:
#         while self.currentNode.next and steps > 0:
#             self.currentNode = self.currentNode.next
#             steps -= 1
#         return self.currentNode.val

#### Two Stack ####
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = homepage
        self.history = []
        self.future = []

    def visit(self, url: str) -> None:
        self.history.append(self.current)
        self.current = url
        self.future = []

    def back(self, steps: int) -> str:
        while self.history and steps > 0:
            self.future.append(self.current)
            self.current = self.history.pop()
            steps -= 1
        if not self.current:
            self.current = self.future.pop()
        return self.current

    def forward(self, steps: int) -> str:
        while self.future and steps > 0:
            self.history.append(self.current)
            self.current = self.future.pop()
            steps -= 1
        if not self.current:
            self.current = self.history.pop()
        return self.current

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)