# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #### DFS creat and sort ####
        ans = []
        cache = ""
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
                elif not node.left and not node.right:
                    ans.append(path)
        for i in range(len(ans)):
            for j in range(-1, -len(ans[i]) - 1, -1):
                cache = cache + chr(ans[i][j] + 97)
            ans[i] = cache
            cache = ""
        ans.sort()
        return ans[0]