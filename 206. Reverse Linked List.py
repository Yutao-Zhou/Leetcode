# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### get value and creat, not real solution ####
        # if head == None:
        #     return ListNode("")
        # value = []
        # while head:
        #     value.append(head.val)
        #     head = head.next
        # value = value[::-1]
        # ans = ListNode(value[0])
        # realAns = ans
        # realAns.next = ans
        # for i in value:
        #     ans.next = ListNode(i)
        #     ans = ans.next
        # return realAns.next
        
        #### swap ####
        previous = None
        while head:
            current = head
            head = head.next
            current.next = previous
            previous = current
        return previous