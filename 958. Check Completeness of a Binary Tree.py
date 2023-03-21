# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #### Level tranversal with trigger ####
        queue = deque([(root, 0)])
        trigger = False
        while queue:
            node, level = queue.popleft()
            if not node:
                trigger = True
            if node:
                if trigger:
                    return False
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
        return True