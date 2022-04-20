# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        #### recursive modify value ####
        def recursion(root):
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left  = recursion(root.left)
            if root.right:
                right = recursion(root.right)
            root.val = root.val + left + right
            return root.val
        recursion(root)
        def subtract(root):
            if not root:
                return
            left = 0
            right = 0
            if root.left:
                left  = root.left.val
                subtract(root.left)
            if root.right:
                right = root.right.val
                subtract(root.right)
            ans.append(abs(left - right))
            return root
        global ans
        ans = []
        subtract(root)
        return sum(ans)
        
        #### Lingcai's recursion ####
        # self.ans = 0
        # def getSum(root):
        #     if not root: return 0
        #     left_sum = getSum(root.left)
        #     right_sum = getSum(root.right)
        #     self.ans += abs(left_sum - right_sum)
        #     print(left_sum, root.val, right_sum)
        #     return left_sum + root.val + right_sum
        # getSum(root)
        # return self.ans
        