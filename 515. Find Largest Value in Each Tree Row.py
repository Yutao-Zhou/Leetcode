# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #### BFS level interation ####
        if not root:
            return []
        ans = []
        m = float("-inf")
        levelNum = 1
        que = deque([root])
        while que:
            node = que.popleft()
            if node.val > m:
                    m = node.val
            levelNum -= 1
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            if levelNum == 0:
                ans.append(m)
                m = float("-inf")
                levelNum = len(que)
        return ans