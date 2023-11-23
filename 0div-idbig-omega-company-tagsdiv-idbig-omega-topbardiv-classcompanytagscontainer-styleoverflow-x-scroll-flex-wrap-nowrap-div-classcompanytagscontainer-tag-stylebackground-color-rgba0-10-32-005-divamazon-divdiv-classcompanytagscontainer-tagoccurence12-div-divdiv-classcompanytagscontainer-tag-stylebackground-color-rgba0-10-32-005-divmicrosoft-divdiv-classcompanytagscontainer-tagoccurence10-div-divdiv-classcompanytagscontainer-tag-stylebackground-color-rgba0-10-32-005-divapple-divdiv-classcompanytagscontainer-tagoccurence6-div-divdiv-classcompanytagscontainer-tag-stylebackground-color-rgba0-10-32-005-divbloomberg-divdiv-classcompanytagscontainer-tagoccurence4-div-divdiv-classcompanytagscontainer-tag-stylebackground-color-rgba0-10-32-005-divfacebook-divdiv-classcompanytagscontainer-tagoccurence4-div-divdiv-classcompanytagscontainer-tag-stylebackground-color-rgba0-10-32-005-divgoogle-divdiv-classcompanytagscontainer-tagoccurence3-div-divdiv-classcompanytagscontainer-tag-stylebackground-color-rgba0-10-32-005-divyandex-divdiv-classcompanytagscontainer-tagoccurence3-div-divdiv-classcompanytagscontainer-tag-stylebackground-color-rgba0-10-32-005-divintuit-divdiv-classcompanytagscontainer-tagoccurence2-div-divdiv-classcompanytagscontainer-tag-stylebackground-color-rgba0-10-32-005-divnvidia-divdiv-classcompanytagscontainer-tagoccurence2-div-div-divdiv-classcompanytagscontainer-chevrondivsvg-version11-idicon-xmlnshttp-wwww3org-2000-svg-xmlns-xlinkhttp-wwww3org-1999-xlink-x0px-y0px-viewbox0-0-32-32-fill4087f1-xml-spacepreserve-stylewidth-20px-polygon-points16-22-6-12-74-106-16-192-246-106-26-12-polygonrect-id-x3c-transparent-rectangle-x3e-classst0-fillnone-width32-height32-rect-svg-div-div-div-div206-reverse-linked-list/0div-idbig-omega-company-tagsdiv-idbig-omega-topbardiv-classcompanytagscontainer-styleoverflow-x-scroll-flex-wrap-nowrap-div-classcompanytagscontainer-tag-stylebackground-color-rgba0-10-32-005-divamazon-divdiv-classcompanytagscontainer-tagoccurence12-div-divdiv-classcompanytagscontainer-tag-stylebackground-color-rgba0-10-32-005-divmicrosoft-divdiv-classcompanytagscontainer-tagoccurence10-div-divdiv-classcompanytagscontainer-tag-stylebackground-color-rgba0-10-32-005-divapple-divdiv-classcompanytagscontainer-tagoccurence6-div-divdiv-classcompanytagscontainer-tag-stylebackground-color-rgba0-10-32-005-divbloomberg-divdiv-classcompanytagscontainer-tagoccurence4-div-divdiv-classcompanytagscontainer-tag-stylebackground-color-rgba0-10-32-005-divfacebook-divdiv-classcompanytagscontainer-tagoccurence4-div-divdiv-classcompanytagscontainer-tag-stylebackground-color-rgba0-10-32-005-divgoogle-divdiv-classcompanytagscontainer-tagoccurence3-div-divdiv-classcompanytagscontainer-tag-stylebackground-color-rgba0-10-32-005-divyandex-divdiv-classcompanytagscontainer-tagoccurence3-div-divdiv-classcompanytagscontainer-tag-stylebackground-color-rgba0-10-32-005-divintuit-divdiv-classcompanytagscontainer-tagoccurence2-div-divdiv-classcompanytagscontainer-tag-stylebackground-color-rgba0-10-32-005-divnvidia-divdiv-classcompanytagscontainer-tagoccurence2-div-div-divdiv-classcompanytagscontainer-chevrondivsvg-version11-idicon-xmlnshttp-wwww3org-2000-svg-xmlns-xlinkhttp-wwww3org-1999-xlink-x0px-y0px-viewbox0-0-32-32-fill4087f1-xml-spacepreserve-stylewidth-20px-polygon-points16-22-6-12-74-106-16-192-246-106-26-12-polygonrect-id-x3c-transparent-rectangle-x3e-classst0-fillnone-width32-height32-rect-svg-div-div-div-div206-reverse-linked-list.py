class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: #reached end
            return head
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head