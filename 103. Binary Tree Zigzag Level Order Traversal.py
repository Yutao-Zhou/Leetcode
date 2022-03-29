# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #### BFS ####
        ans = []
        path = []
        que = deque()
        que.append(root)
        level = 1
        deep = 1
        while que:
            node = que.popleft()
            if node:
                level -= 1
                path.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if level == 0:
                    level = len(que)
                    if deep % 2 == 0:
                        ans.append(path[::-1])
                    if deep % 2 == 1:
                        ans.append(path)
                    path = []
                    deep += 1
        return ans