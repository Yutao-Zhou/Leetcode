# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #### inorder map ####
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         sort.append(root.val)
        #         inorder(root.right)
        #         return sort
        # sort = []
        # inorder(root)
        # i = 0
        # j = len(sort) - 1
        # while i < j:
        #     if sort[i] + sort[j] == k:
        #         return True
        #     elif sort[i] + sort[j] < k:
        #         i += 1
        #     elif sort[i] + sort[j] > k:
        #         j -= 1
        # return False
        
        #### BST BFS ####
        seen = set()
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if k - node.val in seen:
                return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            seen.add(node.val)
        return False