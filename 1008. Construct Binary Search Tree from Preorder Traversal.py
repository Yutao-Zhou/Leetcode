# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #### Find and Devide ####
        # def construct(preorder):
        #     lenPreorder = len(preorder)
        #     if lenPreorder == 1:
        #         return TreeNode(preorder[0])
        #     i = 1
        #     while i < lenPreorder and preorder[i] < preorder[0]:
        #         i += 1
        #     root = TreeNode(preorder[0])
        #     if preorder[1 : i]:
        #         root.left = construct(preorder[1 : i])
        #     if preorder[i:]:
        #         root.right = construct(preorder[i:])
        #     return root
        # return construct(preorder)
        
        #### Two Pointers ####
        def construct(i, j):
            if i == j:
                return
            mid = i + 1
            while mid < lenPreorder and preorder[mid] < preorder[i]:
                mid += 1
            root = TreeNode(preorder[i])
            if mid > i:
                root.left = construct(i + 1, mid)
            if j > mid:
                root.right = construct(mid, j)
            return root
        lenPreorder = len(preorder)
        return construct(0, lenPreorder)