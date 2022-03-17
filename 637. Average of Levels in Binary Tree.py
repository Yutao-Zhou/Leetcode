# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #### BFS with level node ####
        que = []
        que.append(root)
        levelNode = 1
        num = 0
        level = []
        ans = []
        while que:
            node = que.pop(0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            level.append(node.val)
            levelNode -= 1
            num += 1
            if levelNode == 0:
                levelNode = len(que)
                ans.append(sum(level)/num)
                num = 0
                level = []
        return ans