"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copied = {}
        last = None
        while head:
            if head not in copied:
                copied[head] = Node(head.val, head.next, head.random)
            if last:
                copied[last].next = copied[head] 
            if not last:
                start = copied[head]
            if head.random:
                if head.random not in copied:
                    copied[head.random] = Node(head.random.val, head.random.next, head.random.random)
                copied[head].random = copied[head.random]
            last = head
            head = head.next
        return start