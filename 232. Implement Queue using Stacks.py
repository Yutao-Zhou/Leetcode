class MyQueue:
    #### deque ####
#     def __init__(self):
#         self.stack = deque()
        
#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         return self.stack.popleft()

#     def peek(self) -> int:
#         return self.stack[0]

#     def empty(self) -> bool:
#         return self.stack == deque()
    
    #### Two Stacks ####
    def __init__(self):
        self.stack = [] # real stack
        self.cache = [] # cache stack
        
    def push(self, x: int) -> None:
        while self.stack:
            self.cache.append(self.stack.pop())
        self.stack.append(x)
        while self.cache:
            self.stack.append(self.cache.pop())

    def pop(self) -> int:
        return self.stack.pop()
    
    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()