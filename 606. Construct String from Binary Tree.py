# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        #### Recursive ####
        # def build(node):
        #     if not node.left and not node.right:
        #         return f"{node.val}"
        #     if node.left and node.right:
        #         return f"{node.val}({build(node.left)})({build(node.right)})"
        #     if node.left:
        #         return f"{node.val}({build(node.left)})"
        #     return f"{node.val}()({build(node.right)})"
        # return build(root)
        
        #### Iteritived ####
        ans, stack = "", [(root, False)]
        while stack:
            if stack[-1][1]:
                ans = ans + ")"
                stack.pop()
            else:
                curr = stack[-1][0]
                ans = ans + f"({curr.val}"
                stack[-1] = (curr, True)
                if curr.right:
                    stack.append((curr.right, False))
                    if not curr.left:
                        ans = ans + "()"
                if curr.left:
                    stack.append((curr.left, False))
        return ans[1 : -1]