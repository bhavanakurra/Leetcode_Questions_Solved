# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        res = head
        while list1 and list2:
            if list1.val < list2.val:
                # res = ListNode(list1.val)
                res.next = list1 #res = list1 changed
                list1 = list1.next
                res = res.next
                # res.next = res
            else:
                # res.next = ListNode(list2.val)
                res.next = list2
                list2 = list2.next
                res = res.next
                # res.next = res
                
        if list1:
            res.next=list1
        if list2:
            res.next=list2
                
#         while list1:
#             res = ListNode(list1.val)
#             res.next = res
        
#         while l2:
#             res = ListNode(list2.val)
#             res.next = res
            
        return head.next
        