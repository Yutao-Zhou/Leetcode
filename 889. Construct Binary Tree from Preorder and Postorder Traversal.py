# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(preStart, preEnd, postStart, postEnd):
            if preStart > preEnd:
                return
            root = TreeNode(preorder[preStart])
            if preStart == preEnd:
                return root
            leftRootIndex = postorderMap[preorder[preStart + 1]]
            leftSize = leftRootIndex - postStart + 1
            root.left = build(preStart + 1, preStart + leftSize, postStart, leftRootIndex)
            root.right = build(preStart + leftSize + 1, preEnd, leftRootIndex + 1, postEnd - 1)
            return root
        preorderIndex = 0
        postorderMap = {}
        for i in range(len(postorder)):
            postorderMap[postorder[i]] = i
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)