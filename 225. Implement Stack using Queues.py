class MyStack:

    def __init__(self):
        self.que = deque()
        self.cache = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        while self.que:
            current  = self.que.popleft()
            if self.que:
                self.cache.append(current)
        self.que = self.cache
        self.cache = deque()
        return current

    def top(self) -> int:
        while self.que:
            current  = self.que.popleft()
            self.cache.append(current)
        self.que = self.cache
        self.cache = deque()
        return current

    def empty(self) -> bool:
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()