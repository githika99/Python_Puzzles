# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        #use fast and slow pointer
        odd = head
        #even_start = head.next
        even = head.next
        #even_start.next = even
        #smt like 
        while odd and odd.next:
            print ("odd is", odd.val)
            print ("even is", even.val)
            odd.next = even.next
            even.next = odd.next
        odd.next = even
        return head

if __name__ == "__main__":
    lst = [2,3,4,5]
    head = ListNode(1)
    for x in lst:
        head.next = ListNode(x)
    print(Solution.oddEvenList(head))
    