# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #### BFS not BST ####
        ans = float("inf")
        BFS = []
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                BFS.append(node.val)
                que.append(node.left)
                que.append(node.right)
        print(BFS)
        for i in range(len(BFS)):
            for j in range(i + 1,len(BFS)):
                if abs(BFS[i] - BFS[j]) < ans:
                    ans = abs(BFS[i] - BFS[j])
        return ans