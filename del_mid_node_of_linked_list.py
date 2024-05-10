# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#my solution
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        node = head
        while node.next:        #while node.next != NULL
            length += 1
            node = node.next

        middle = floor(length/2)
        mid_node = head
        
        if middle != 0:
            i = 0
            while i < middle - 1:        #mid_node is one before mid_node
                mid_node = mid_node.next
                i += 1
            
            mid_node.next = mid_node.next.next      #prev.next = one after, could be null
            return head

        return mid_node.next