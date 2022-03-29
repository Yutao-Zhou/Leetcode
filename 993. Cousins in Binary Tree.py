# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #### BFS ####
        deep = 0
        parent = None
        que = deque()
        que.append((root, deep, parent))
        compare = []
        while que:
            node = que.popleft()
            current = node[0]
            deep = node[1]
            parent = node[2]
            if current:
                parent = current.val
                if current.left:
                    que.append((current.left, deep + 1, parent))
                if current.right:
                    que.append((current.right, deep + 1, parent))
                if current.val == x or current.val == y:
                    compare.append(node)
        return compare[0][1] == compare[1][1] and compare[0][2] != compare[1][2]