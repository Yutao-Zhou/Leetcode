# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        position = 0
        while head:
            ans.append(0)
            while stack:
                if head.val > stack[-1][0]:
                    ans[stack[-1][1]] = head.val
                    stack.pop()
                else:
                    break
            stack.append((head.val, position))
            head = head.next
            position += 1
        return ans