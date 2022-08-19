# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #### DFS and Recursive Check ####
        # def isIdentical(r, s): # Recursion get wither they are same tree
        #     if (not r and s) or (not s and r):
        #         return False
        #     if not s and not r:
        #         return True
        #     else:
        #         if r.val != s.val:
        #             return False
        #         lc = isIdentical(r.left, s.left)
        #         rc = isIdentical(r.right, s.right)
        #         return lc and rc
        # que = deque([root]) # DFS
        # while que:
        #     node = que.popleft()
        #     if node:
        #         que.append(node.left)
        #         que.append(node.right)
        #         if node.val == subRoot.val:
        #             if isIdentical(node, subRoot):
        #                 return True
        # return False
        
        #### Conver to string and check wither it is substring ####
        def toString(node):
            if node:
                return f"#{node.val} {toString(node.left)} {toString(node.right)}"
        return toString(subRoot) in toString(root)
            