# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #### DFS ####
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if val < node.val:
                    if node.left:
                        stack.append(node.left)
                    else:
                        return None
                if val > node.val:
                    if node.right:
                        stack.append(node.right)
                    else:
                        return None
                if val == node.val:
                    return node