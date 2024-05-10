#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self is None:
            return f"None, next = {self.next.val}"
        if self.next is None:
            return f"{self.val}, next = None"
        else:
            return f"{self.val}, next = {self.next.val}"
        
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        prnt = head
        while prnt:
            print(prnt.val, end=" ")
            prnt = prnt.next

        if not head:
            return head

        #we should implement this so that if the first node is repeated, we can delete it
        hleft = ListNode(val = None, next = head)               
        slow = hleft
        cmp = head
        ptr = head

        curr_val = cmp.val

        while ptr.next:
            ptr = ptr.next                  #iterate to the next element
            if ptr.val == curr_val:
                cmp.next = ptr.next        #deletes ptr
                ptr = ptr.next
                while ptr.val == curr_val:
                    cmp.next = ptr.next                 #skips all duplicates of ptr
                    ptr = ptr.next
                slow.next = ptr
                cmp = ptr
                curr_val = cmp.val
                
            else:
                slow = cmp                   #slow iterates one
                cmp = ptr
                curr_val = cmp.val
        
        return hleft.next

if __name__ == "__main__":
    lst = [1,2,3,3,4,4,5]
    head = ListNode(val = lst[0])
    curr = head
    for x in range(1,len(lst)):
        curr.next= ListNode(val = lst[x])
        curr = curr.next
    
    solution = Solution()                       #make an instance of Solution()
    
    new_head = solution.deleteDuplicates(head)
    print("main funct reached")
    #print new_head
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next