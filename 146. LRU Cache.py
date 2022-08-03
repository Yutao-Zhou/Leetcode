class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.l, self.r = Node(0,0), Node(0,0)
        self.l.next= self.r
        self.r.next = self.l
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove key node from linked list
            self.cache[key].pre.next = self.cache[key].next
            self.cache[key].next.pre = self.cache[key].pre
            # add to front
            self.cache[key].pre = self.l
            self.cache[key].next = self.l.next
            self.l.next = self.cache[key]
            self.cache[key].next.pre = self.cache[key]
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key].val = value
            # remove key node from linked list
            self.cache[key].pre.next = self.cache[key].next
            self.cache[key].next.pre = self.cache[key].pre
            # add to front
            self.cache[key].pre = self.l
            self.cache[key].next = self.l.next
            self.l.next = self.cache[key]
            self.cache[key].next.pre = self.cache[key]
        elif len(self.cache) >= self.capacity: # exceed capacity
            self.cache.pop(self.r.pre.key)
            # remove end
            self.r.pre.next = None
            self.r.pre = self.r.pre.pre
            self.r.pre.next.pre = None
            self.r.pre.next = self.r
            # add to start
            self.cache[key] = Node(key, value)
            self.cache[key].next = self.l.next
            self.cache[key].pre = self.l
            self.cache[key].next.pre = self.cache[key]
            self.l.next = self.cache[key]
        else: # normal add not exceeding capacity
            self.cache[key] = Node(key, value)
            self.cache[key].next = self.l.next
            self.cache[key].pre = self.l
            self.cache[key].next.pre = self.cache[key]
            self.l.next = self.cache[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)