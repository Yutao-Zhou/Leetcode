# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### Two pointer one at start one at end ####
        # if head:
        #     length = 1
        #     ans = head
        #     left = head
        #     while head.next:
        #         length += 1
        #         head = head.next
        #     swap = length // 2
        #     while left.next and left.next.next and swap > 0:
        #         tmp = left.next.next
        #         head.next = left.next
        #         head.next.next = None
        #         left.next = tmp
        #         left = left.next 
        #         head = head.next
        #         swap -= 1
        # else:
        #     return head
        # return ans

        #### Two pointer even and odd ####
        if head:
            ans = head
            odd = head
            even = head.next
            even_head = even
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = even_head
        else:
            return head
        return ans