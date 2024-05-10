# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        bl = ListNode(val = None, next = head)
        l = head
        r = head
        while True: 
            print(left,right)                                         #while l and r are not 0
            if left != 1:
                left -= 1
                l = l.next
            if right != 1:
                right -= 1
                r = r.next
            elif left == 1 and right == 1:
                break

        print("bl is", bl)
        print("l is", l)
        print("r is", r)

        ptr = l
        ar = r.next             #could be None, which would be okay
            
        while bl and ptr:
            if bl.next != l:
                bl = bl.next
            if ptr.next != r:
                ptr = ptr.next
        
        print("bl is", bl)
        print("l is", l)
        print("ptr is", ptr)
        print("r is", r)
        print("ar is", ar)
        
        """
        while l != r:
            bl.next = r
            r.next = l
            ptr.next = ar

            #reassign
            bl = bl.next
            ptr = l
            r = l
            while ptr and r:
                if r.next != ar:
                    r = r.next
                if ptr.next.next != ar:
                    ptr = ptr.next
        """
        
        return head
                

