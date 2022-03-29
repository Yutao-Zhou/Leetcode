# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #### BFS ####
        level = 1
        cache = []
        ans = deque()
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                level -= 1
                cache.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if level == 0:
                    ans.appendleft(cache)
                    cache = []
                    level = len(que)
        return ans