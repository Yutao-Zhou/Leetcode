# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #### DFS get all path and calculate ####
        # ans = 0
        # allNum = []
        # path = [root.val]
        # stack = [(root, path)]
        # while stack:
        #     current = stack.pop()
        #     node = current[0]
        #     path = current[1]
        #     if node:
        #         if node.left:
        #             stack.append((node.left, path + [node.left.val]))
        #         if node.right:
        #             stack.append((node.right, path + [node.right.val]))
        #         elif node.left == None and node.right == None:
        #             allNum.append(path)
        # for i in range(len(allNum)):
        #     for j in range(-1, -len(allNum[i]) - 1, -1):
        #         ans += allNum[i][j] * 10 ** (abs(j) - 1)
        # return ans
    
        #### DFS calculate while iterating ####
        ans = 0
        path = [root.val]
        stack = [(root, path)]
        while stack:
            current = stack.pop()
            node = current[0]
            path = current[1]
            if node:
                if node.left:
                    stack.append((node.left, path + [node.left.val]))
                if node.right:
                    stack.append((node.right, path + [node.right.val]))
                elif node.left == None and node.right == None:
                    for i in range(-1, -len(path) - 1, -1):
                        ans += path[i] * 10 ** (abs(i) - 1)
        return ans