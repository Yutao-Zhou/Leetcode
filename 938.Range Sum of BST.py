# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #### preorder DFS ####
        # stack = []
        # cache = []
        # ans = []
        # stack.append(root)
        # while stack != []:
        #     node = stack.pop()
        #     if node != None:
        #         if low <= node.val <= high:
        #             cache.append(node.val)
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return sum(cache)
        #### preorder BST ####
        stack = []
        cache = []
        ans = []
        stack.append(root)
        while stack != []:
            node = stack.pop()
            if node != None:
                if low <= node.val <= high:
                    cache.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
                if node.val < low:
                    stack.append(node.right)
                if node.val > high:
                    stack.append(node.left)
        return sum(cache)