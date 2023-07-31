"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        queue = deque()
        queue.append((root, 0))
        level = []
        current_level = 0
        if not root:
            return []
        while queue:
            current = queue.popleft()
            if current[1] > current_level:
                ans.append(level)
                level = []
                current_level += 1
            for node in current[0].children:
                queue.append((node, current[1] + 1))
            level.append(current[0].val)
        ans.append(level)
        return ans