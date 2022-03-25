# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #### BFS with level and check ####
        # ans = []
        # cache = []
        # que = deque()
        # que.append(root)
        # level = len(que)
        # counter = 0
        # while que:
        #     node = que.popleft()
        #     cache.append(node.val)
        #     counter += 1
        #     if node.left:
        #         que.append(node.left)
        #     if node.right:
        #         que.append(node.right)
        #     if counter == level:
        #         counter = 0
        #         level = len(que)
        #         ans.append(cache)
        #         cache = []
        # for i in range(len(ans)):
        #     for j in range(len(ans[i])):
        #         if i % 2 == 0:
        #             if ans[i][j] % 2 == 0 or (j != 0 and ans[i][j] <= ans[i][j - 1]):
        #                 return False
        #         if i % 2 == 1:
        #             if ans[i][j] % 2 == 1 or (j != 0 and ans[i][j] >= ans[i][j - 1]):
        #                 return False
        # return True
        
        #### BFS check while interating ####
        if root.val % 2 == 0:
            return False
        que = deque()
        que.append(root)
        level = len(que)
        counter = 0
        deepth = 1
        start = True
        while que:
            node = que.popleft()
            counter += 1
            if node.left:
                if node.left.val % 2 == deepth % 2:
                    return False
                if start == False:
                    if deepth % 2 == 0 and node.left.val <= que[-1].val:
                        return False
                    if deepth % 2 == 1 and node.left.val >= que[-1].val:
                        return False
                que.append(node.left)
                start = False
            if node.right:
                if node.right.val % 2 == deepth % 2:
                    return False
                if start == False:
                    if deepth % 2 == 0 and node.right.val <= que[-1].val:
                        return False
                    if deepth % 2 == 1 and node.right.val >= que[-1].val:
                        return False
                que.append(node.right)
                start = False
            if counter == level:
                counter = 0
                deepth += 1
                start = True
                level = len(que)
        return True