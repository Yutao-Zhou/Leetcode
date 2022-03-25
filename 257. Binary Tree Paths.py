# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #### DFS iterate and generate ####
        cache = ""
        ans = []
        path = [root.val]
        stack = [(root, path)]
        while stack:
            current = stack.pop()
            node = current[0]
            if node:
                path = current[1]
                if node.left:
                    stack.append((node.left, path + [node.left.val]))
                if node.right:
                    stack.append((node.right, path + [node.right.val]))
                if not node.left and not node.right:
                    for i in path:
                        cache = cache + str(i) + "->"
                    ans.append(cache[:-2])
                    cache = ""
        return ans