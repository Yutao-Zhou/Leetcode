# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #### DFS Brute Force####
        # ans = 0
        # path = [root.val]
        # stack = [(root, path)]
        # while stack:
        #     node = stack.pop()
        #     current = node[0]
        #     if current:
        #         path = node[1]
        #         if current.left:
        #             stack.append((current.left, path + [current.left.val]))
        #         if current.right:
        #             stack.append((current.right, path + [current.right.val]))
        #         if not current.left and not current.right:
        #             for i in range(len(path)):
        #                 for j in range(i + 1, len(path)):
        #                     if abs(path[i] - path[j]) > ans:
        #                         ans = abs(path[i] - path[j])
        # return ans
        
        #### DFS min and max ####
        ans = 0
        minimum = root.val
        maximum = root.val
        stack = [(root, minimum, maximum)]
        while stack:
            node = stack.pop()
            current = node[0]
            minimum = node[1]
            maximum = node[2]
            if current:
                path = node[1]
                if current.left:
                    stack.append((current.left, min(minimum, current.left.val), max(maximum, current.left.val)))
                if current.right:
                    stack.append((current.right, min(minimum, current.right.val), max(maximum, current.right.val)))
                if not current.left and not current.right:
                    if abs(maximum - minimum) > ans:
                                ans = abs(maximum - minimum)
        return ans