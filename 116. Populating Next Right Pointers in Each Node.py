"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #### Tranverse In Level ####
        queue = deque([(root, 0)])
        while queue:
            node = queue.popleft()
            if node[0]:
                queue.append((node[0].left, node[1] + 1))
                queue.append((node[0].right, node[1] + 1))
                if queue:
                    if queue[0][1] == node[1]:
                        node[0].next = queue[0][0]
                        continue
                node[0].next = None
        return root