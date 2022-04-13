# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #### BFS recursive ####
        # def recursive(root):
        #     if root.right:
        #         recursive(root.right)
        #     global cache
        #     cache += root.val
        #     root.val =  cache
        #     if root.left:
        #         recursive(root.left)
        #     return root
        # global cache
        # cache = 0
        # return recursive(root)
        
        #### iteritive DFS inorder ####
        counter = 0
        stack = [(root, "start")]
        while stack:
            node = stack.pop()
            if node[0]:
                if node[1] == "m":
                    counter += node[0].val
                    node[0].val = counter
                else:
                    stack.append((node[0].left, "l"))
                    stack.append((node[0], "m"))
                    stack.append((node[0].right, "r"))
        return root