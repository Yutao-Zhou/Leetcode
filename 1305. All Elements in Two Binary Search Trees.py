# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        #### DFS recursive ####
        # i = 0
        # j = 0
        # stack = []
        # list1 = []
        # list2 = []
        # ans = []
        # def DFS(root, l):
        #     stack.append(root)
        #     while stack:
        #         node = stack.pop()
        #         if node:
        #             l.append(node.val)
        #             DFS(node.left, l)
        #             DFS(node.right, l)
        # def bubble_sort(l):
        #     for i in range(len(l)):
        #         for j in range(i,len(l)):
        #             if l[i] > l[j]:
        #                 l[i], l[j] = l[j], l[i]
        #     return l
        # DFS(root1, list1)
        # DFS(root2, list2)
        # bubble_sort(list1)
        # bubble_sort(list2)
        # while 1:
        #     if i == len(list1):
        #         ans.extend(list2[j:])
        #         return ans
        #     if j == len(list2):
        #         ans.extend(list1[i:])
        #         return ans
        #     elif list1[i] >= list2[j]:
        #         ans.append(list2[j])
        #         j += 1
        #     elif list1[i] < list2[j]:
        #         ans.append(list1[i])
        #         i += 1
        
        #### DFS faster ####
        # i = 0
        # j = 0
        # stack = []
        # list1 = []
        # def DFS(root, l):
        #     stack.append(root)
        #     while stack:
        #         node = stack.pop()
        #         if node:
        #             l.append(node.val)
        #             DFS(node.left, l)
        #             DFS(node.right, l)
        #     return l
        # DFS(root1, list1)
        # DFS(root2, list1)
        # return sorted(list1)
    
        #### two tree together ####
        ans = []
        stack1 = []
        stack2 = []
        while root1 or root2 or stack1 or stack2:
            while root1:        ### put all left node of root1 in stack1 bc BST
                stack1.append(root1)
                root1 = root1.left
            while root2:        ### put all left node of root2 in stack2 bc BST
                stack2.append(root2)
                root2 = root2.left
            if stack2 == [] or (len(stack1) > 0 and stack1[-1].val <= stack2[-1].val):  #### if finished stack2 or stack1 is still smaller or equal to stack2
                root1 = stack1.pop()
                ans.append(root1.val)       ### put root1 and left node in
                root1 = root1.right         ### tranverse right node of root1
            else:
                root2 = stack2.pop()
                ans.append(root2.val) ### put root2 and left node in
                root2 = root2.right ### tranverse right node of root2
        return ans
            