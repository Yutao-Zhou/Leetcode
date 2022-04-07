# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #### BFS both ####
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # que1 = deque([root1])
        # que2 = deque([root2])
        # while que1 and que2:
        #     node1 = que1.popleft()
        #     node2 = que2.popleft()
        #     if node1 and node2:
        #         node1.val += node2.val
        #         if not node1.left and node2.left:
        #             node1.left = TreeNode(0)
        #         if not node1.right and node2.right:
        #             node1.right = TreeNode(0)
        #         que1.append(node1.left)
        #         que1.append(node1.right)
        #         que2.append(node2.left)
        #         que2.append(node2.right)
        # return root1
        
        #### DFS both ####
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # stack1 = [root1]
        # stack2 = [root2]
        # while stack1 and stack2:
        #     node1 = stack1.pop()
        #     node2 = stack2.pop()
        #     if node1 and node2:
        #         node1.val += node2.val
        #         if not node1.left and node2.left:
        #             node1.left = TreeNode(0)
        #         if not node1.right and node2.right:
        #             node1.right = TreeNode(0)
        #         stack1.append(node1.left)
        #         stack1.append(node1.right)
        #         stack2.append(node2.left)
        #         stack2.append(node2.right)
        # return root1
        
        #### recursive ####
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2