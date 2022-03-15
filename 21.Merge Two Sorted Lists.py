# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #### merge one by one ####
        # ans = ListNode(0)
        # ans.next = list1
        # realAns = ans
        # realAns.next = ans
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         ans.next = list1
        #         list1 = list1.next
        #     else:
        #         ans.next = list2
        #         list2 = list2.next
        #     ans =  ans.next
        # ans.next = list1 or list2
        # return realAns.next
        
        #### merge ####
        if list1 == None or list2 == None:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2