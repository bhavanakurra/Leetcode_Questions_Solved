# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node1 = l1
        curr_node2 = l2
        carrier = 0
        dummy = ListNode()
        result = dummy
        #print(result)
        while curr_node1 or curr_node2 or carrier:
            if not curr_node1:
                val1 = 0
            else:
                val1 = curr_node1.val
            if not curr_node2:
                val2 = 0
            else:
                val2 = curr_node2.val
            
            final_value = (val1+val2+carrier)
            print(val1, val2, carrier)
            if final_value>=10:
                carrier = (final_value)//10
                final_value -= 10
            else:
                carrier = 0
            print(val1, val2, carrier, final_value)
            print("----")
            if curr_node1:
                curr_node1 = curr_node1.next
            else:
                curr_node1=None
            if curr_node2:
                curr_node2 = curr_node2.next
            else:
                curr_node2=None
            
            result.next = ListNode(final_value)
            result = result.next
            
        print(dummy.next)
        
        return dummy.next
            
            
        
            