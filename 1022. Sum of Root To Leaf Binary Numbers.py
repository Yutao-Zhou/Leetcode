# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        #### DFS process at every end leaf ####
        s = 0
        stack = []
        path = [root.val]
        stack.append((root, path))
        while stack:
            node = stack.pop()
            current = node[0]
            path = node[1]
            if current:
                if current.left:
                     stack.append((current.left, path + [current.left.val]))
                if current.right:
                     stack.append((current.right, path + [current.right.val]))
                if not current.left and not current.right:
                    num = ""
                    for n in path:
                        if n == 1:
                            num = num + "1"
                        if n == 0:
                            num = num + "0"
                    s += int(num, 2)
        return s