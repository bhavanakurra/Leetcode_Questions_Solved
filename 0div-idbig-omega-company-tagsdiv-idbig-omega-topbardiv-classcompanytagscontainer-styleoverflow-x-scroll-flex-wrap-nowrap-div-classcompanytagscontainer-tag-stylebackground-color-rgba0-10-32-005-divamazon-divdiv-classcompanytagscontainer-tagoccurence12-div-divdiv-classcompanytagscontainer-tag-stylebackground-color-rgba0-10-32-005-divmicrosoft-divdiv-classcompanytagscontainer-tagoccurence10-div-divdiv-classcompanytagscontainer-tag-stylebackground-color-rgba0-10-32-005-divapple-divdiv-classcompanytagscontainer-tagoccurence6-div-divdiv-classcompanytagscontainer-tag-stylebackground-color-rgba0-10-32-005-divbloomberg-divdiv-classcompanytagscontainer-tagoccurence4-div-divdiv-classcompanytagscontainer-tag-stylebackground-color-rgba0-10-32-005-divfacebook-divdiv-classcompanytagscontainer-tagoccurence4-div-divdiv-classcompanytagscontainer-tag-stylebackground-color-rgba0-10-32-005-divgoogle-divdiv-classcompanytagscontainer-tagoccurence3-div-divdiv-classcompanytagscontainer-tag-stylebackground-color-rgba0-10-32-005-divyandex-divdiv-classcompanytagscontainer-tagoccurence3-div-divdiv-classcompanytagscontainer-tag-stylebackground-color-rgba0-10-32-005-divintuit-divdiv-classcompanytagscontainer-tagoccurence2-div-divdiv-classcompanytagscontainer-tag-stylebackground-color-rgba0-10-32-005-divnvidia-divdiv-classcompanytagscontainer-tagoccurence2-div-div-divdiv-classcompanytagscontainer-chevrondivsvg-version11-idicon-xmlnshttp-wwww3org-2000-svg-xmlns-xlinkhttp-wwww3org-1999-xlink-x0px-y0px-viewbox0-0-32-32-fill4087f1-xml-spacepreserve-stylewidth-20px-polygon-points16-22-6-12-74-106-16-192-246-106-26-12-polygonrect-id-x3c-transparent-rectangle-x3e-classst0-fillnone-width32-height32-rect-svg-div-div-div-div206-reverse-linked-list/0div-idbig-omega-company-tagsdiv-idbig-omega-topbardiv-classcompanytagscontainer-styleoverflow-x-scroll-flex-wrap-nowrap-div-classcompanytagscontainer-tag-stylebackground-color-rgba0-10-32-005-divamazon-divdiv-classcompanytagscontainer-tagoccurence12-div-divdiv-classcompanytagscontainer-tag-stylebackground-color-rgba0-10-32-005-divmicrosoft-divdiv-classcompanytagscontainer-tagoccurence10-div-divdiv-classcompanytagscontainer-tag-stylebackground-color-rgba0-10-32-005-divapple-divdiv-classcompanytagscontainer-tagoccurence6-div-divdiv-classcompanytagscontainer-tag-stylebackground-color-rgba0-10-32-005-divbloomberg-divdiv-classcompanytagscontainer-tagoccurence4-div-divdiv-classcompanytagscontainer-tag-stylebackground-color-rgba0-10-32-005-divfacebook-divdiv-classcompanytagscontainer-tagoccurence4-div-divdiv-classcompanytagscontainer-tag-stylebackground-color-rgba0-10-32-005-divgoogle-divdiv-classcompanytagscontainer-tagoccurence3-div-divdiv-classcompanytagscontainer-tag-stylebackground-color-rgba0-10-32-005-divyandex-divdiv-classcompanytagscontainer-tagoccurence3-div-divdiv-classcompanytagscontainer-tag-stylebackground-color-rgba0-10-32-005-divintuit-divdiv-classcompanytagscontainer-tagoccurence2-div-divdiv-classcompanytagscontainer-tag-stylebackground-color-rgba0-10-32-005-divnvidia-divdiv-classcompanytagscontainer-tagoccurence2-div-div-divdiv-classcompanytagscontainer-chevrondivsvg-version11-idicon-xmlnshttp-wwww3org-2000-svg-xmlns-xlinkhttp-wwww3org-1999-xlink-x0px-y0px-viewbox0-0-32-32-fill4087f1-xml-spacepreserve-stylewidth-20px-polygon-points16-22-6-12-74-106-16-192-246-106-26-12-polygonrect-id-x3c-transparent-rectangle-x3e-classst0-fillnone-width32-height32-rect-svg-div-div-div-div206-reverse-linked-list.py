class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next #storing link for future
            curr.next = prev #reversing link
            
            #sifting pointers
            prev = curr
            curr = tmp             
            
        return prev
            