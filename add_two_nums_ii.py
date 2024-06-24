# https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        len_1 = len_2 = pos = 0
        t1 = l1
        t2 = l2
        while t1 or t2:
            if t1:
                len_1 += 1
                t1 = t1.next
            if t2:
                len_2 += 1
                t2 = t2.next

        print("len 1 is", len_1, "len 2 is", len_2)
        t1 = l1
        t2 = l2
        ans = []
        while len_1 != len_2:
            if len_1 > len_2:
                ans.append(t1.val)
                t1 = t1.next
                len_1 -= 1
                pos += 1
                print("ans is (len1) ", ans)
            else:
                ans.append(t2.val)
                t2 = t2.next
                len_2 -= 1
                pos += 1
                print("ans is (len2) ", ans)

        # now they are both equal
        while t1 and t2:
            ans.append(t1.val + t2.val)
            t1 = t1.next
            t2 = t2.next
            print("ans is before carry", ans)
            ptr = pos
            curr = ans[ptr]
            while curr >= 10:
                ans[ptr] -= 10
                if ptr == 0:
                    ans.insert(0, 1) #inserts 1 to first position
                    pos += 1
                    break
                else:
                    ans[ptr-1] += 1
                ptr -= 1
                curr = ans[ptr]

            print("ans is", ans)
            pos += 1

        # make it a linked list
        tmp = head = ListNode(val = 0, next = None)
        for i in ans:
            new = ListNode(val = i, next = None)
            tmp.next = new
            tmp = tmp.next

        return head.next

        # first find lengths of both lists
        # then add appropriate numbers
        # if a sum is ever >= 10, add 1 to the prev answer
        # store the answer in a python array
        # at the end make it into a linked list

        # time complexity: O(n + m)
        # num passes: 2 per linked list and 1 for answer
        # space complecity: O(max(n, m))


