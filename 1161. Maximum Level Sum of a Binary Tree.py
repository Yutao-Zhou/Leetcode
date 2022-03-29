# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #### BFS ####
        maxSum = (float("-inf"), 1)
        level = 1
        deep = 1
        pathSum = 0
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                pathSum += node.val
                level -= 1
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if level == 0:
                    level = len(que)
                    if pathSum > maxSum[0]:
                        maxSum = (pathSum, deep)
                    pathSum = 0
                    deep += 1
        return maxSum[1]    