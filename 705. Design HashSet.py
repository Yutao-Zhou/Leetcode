class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self):
        self.hash_key = [Node(-1) for i in range(100)]
    
    def add(self, key: int) -> None:
        pointer = self.hash_key[key % 100]
        while pointer and pointer.next and pointer.next.val < key:
            pointer = pointer.next
        if pointer.next and pointer.next.val == key:
            return
        else:
            tmp = pointer.next
            pointer.next = Node(key)
            pointer.next.next = tmp

    def remove(self, key: int) -> None:
        pointer = self.hash_key[key % 100]
        while pointer and pointer.next and pointer.next.val < key:
            pointer = pointer.next
        if pointer.next and pointer.next.val == key:
            tmp = pointer.next
            pointer.next = pointer.next.next
            tmp.next = None

    def contains(self, key: int) -> bool:
        pointer = self.hash_key[key % 100]
        while pointer and pointer.val < key:
            pointer = pointer.next
        if pointer:
            return pointer.val == key
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)