# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        #### DFS ####
        que = []
        self.ans = 0
        def DFS(node, parent, GrandParent):
            que.append(root)
            if node:
                DFS(node.left, node, parent)
                DFS(node.right, node, parent)
                if GrandParent and GrandParent.val % 2 == 0:
                    self.ans  += node.val
        DFS(root, None, None)
        return self.ans