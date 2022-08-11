# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #### Brute Force and revalue ####
        
        # Get part that need to be reversed
#         counter, value = 1, []
#         dummy = ListNode(-1)
#         dummy.next = head
#         while head:
#             if left <= counter <= right:
#                 value.append(head.val)
#             head = head.next
#             counter += 1
#             if counter > right:
#                 break
                
#         # revalue original linked list
#         counter, head = 1, dummy.next
#         while counter < left:
#             head = head.next
#             counter += 1
#         while value:
#             head.val = value.pop()
#             head = head.next
#         return dummy.next
        
        #### one pass in place ####
        if not head or left == right: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left-1): p = p.next
        tail = p.next

        for i in range(right-left):
            tmp = p.next                  # a)
            p.next = tail.next            # b)
            tail.next = tail.next.next    # c)
            p.next.next = tmp             # d)
        return dummy.next