# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #### Recursive left and right ####
        # def build(left, right):
        #     if left > right:
        #         return None
        #     value = preorder.popleft()
        #     root = TreeNode(value)
        #     root.left = build(left, inorderIndex[value] - 1)
        #     root.right = build(inorderIndex[value] + 1, right)
        #     return root
        # preorder = deque(preorder)
        # inorderIndex = {}
        # for i in range(len(inorder)):
        #     inorderIndex[inorder[i]] = i
        # return build(0, len(preorder) - 1)
        
        #### Shorter Recursive ####
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root