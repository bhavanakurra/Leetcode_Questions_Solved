# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        
        #saving pointer
        global_head = head
        
        #length of list
        total_length = 0
        while head:
            total_length+=1 
            head = head.next
            
        print(total_length)
        
        if total_length == 1: #important [1], n=1
            return global_head.next
        
        #Node to remove
        n = total_length - n + 1
        
        #?
        # if n<=0:
        #     return
            
            
        len1 = 0
        prev = ListNode(None)
        curr = global_head
        while curr:
            len1 += 1
            if len1==n:
                if n==1: #Important - [1,2], n=2
                    global_head = curr.next
                else:
                    prev.next = curr.next        
            else:    
                prev = curr
            curr = curr.next 
                
        return global_head
            
            