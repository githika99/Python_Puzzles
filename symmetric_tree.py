# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
        A = [headA]
        B = [headB]
        headA = headA.next
        headB = headB.next

        while headA and headB:
            if headA in B:
                return headA
            elif headB in A:
                return headB
            
            A.append(headA)
            B.append(headB)
            headA = headA.next
            headB = headB.next

        return None

if __name__ == "__main__":
     posA = headA = ListNode(4)
     A = [1,8,4,5]
     for i in A:
          posA.next = ListNode(i)
          posA = posA.next
     posB = headB = ListNode(5)
     B = [6,1,8,4,5]
     for i in B:
          posB.next = ListNode(i)
          posB = posB.next
        
     print(getIntersectionNode(headA, headB))
