# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #### one pass on both list ####
        ans = list1
        a -= 1
        b -= a
        while list1:
            if a == 0:
                cache = list1.next
                list1.next = list2
                while list1.next:
                    list1 = list1.next
                while b:
                    cache = cache.next
                    b -= 1
                list1.next = cache
                return ans
            else:
                a -= 1
                list1 = list1.next