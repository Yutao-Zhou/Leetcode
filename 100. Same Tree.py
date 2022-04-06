# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #### DFS both ####
        if not p and q:
            return False
        stackp = [p]
        stackq = [q]
        while stackp:
            nodep = stackp.pop()
            if not stackq:
                return False
            nodeq = stackq.pop()
            if nodep:
                stackp.append(nodep.left)
                stackp.append(nodep.right)
                if not nodeq :
                    return False
                else:
                    if nodep.val != nodeq.val:
                        return False
                    stackq.append(nodeq.left)
                    stackq.append(nodeq.right)
        stackp = [p]
        stackq = [q]
        while stackq:
            nodep = stackq.pop()
            if not stackp:
                return False
            nodeq = stackp.pop()
            if nodep:
                stackq.append(nodep.left)
                stackq.append(nodep.right)
                if not nodeq :
                    return False
                else:
                    if nodep.val != nodeq.val:
                        return False
                    stackp.append(nodeq.left)
                    stackp.append(nodeq.right)
        return True