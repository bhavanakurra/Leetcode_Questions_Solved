# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        print(head)
        curr = head
        total_length = 0
        while curr:
            curr = curr.next
            total_length = total_length + 1          
        nth_node = (total_length-n)
        
        result = ListNode()
        result_ptr = result
        
        curr1 = head
        count = 0
        print("entered")
        
        while curr1:
            if count!=nth_node:
                result_ptr.next=ListNode(curr1.val)
                result_ptr = result_ptr.next
                
            count = count + 1
            curr1 = curr1.next
        print(result)
        
        
            
        return result.next