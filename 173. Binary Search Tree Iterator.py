# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #### Tranverse and Store ####
#     def __init__(self, root: Optional[TreeNode]):
#         def inOrder(root):
#             if root.left:
#                 inOrder(root.left)
#             self.inorder.append(root.val)
#             if root.right:
#                 inOrder(root.right)
#         self.inorder = []
#         self.pointer = -1
#         inOrder(root)
#         self.lenInorder = len(self.inorder)

#     def next(self) -> int:
#         self.pointer += 1
#         return self.inorder[self.pointer]

#     def hasNext(self) -> bool:
#         return self.pointer + 1 < self.lenInorder
    
    #### Stack ####
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val

    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()