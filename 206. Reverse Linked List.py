# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### recursive ####
        def recursive(head):
            if not head or not head.next:
                return head
            node = recursive(head.next)
            head.next.next = head
            head.next = None
            return node
        return recursive(head)
        
        #### iterative ####
        # prev = None
        # curr = head
        # while curr:
        #     n = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = n
        # return prev
    
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