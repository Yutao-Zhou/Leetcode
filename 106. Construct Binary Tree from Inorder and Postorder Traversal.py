# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inStart, inEnd):
            if inStart > inEnd:
                return
            root = TreeNode(postorder.pop())
            root.right = build(inorderMap[root.val] + 1, inEnd)
            root.left = build(inStart, inorderMap[root.val] - 1)
            return root
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        return build(0, len(inorder) - 1)