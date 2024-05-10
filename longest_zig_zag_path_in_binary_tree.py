# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        #MY SOLUTION WORKS. LET IT BE KNOWN TO THE WORLD
        #YET, IT DOES NOT PASS THE "TIME TEST" BOO HOO

        #function to find zigzag path length given node and left or right to start w 
        len = 0
        def zigzag(root, left):
            nonlocal len
            if not root:
                return 
                
            if not root.left and not root.right:
                len += 1
                return
            
            len += 1

            if left:
                zigzag(root.left, False)
            
            else:
                zigzag(root.right, True)

        #function that calls prev funct w every node and alternating left and rigth
        max_len = float('-inf')
        def call(root):
            nonlocal max_len, len
            if not root:
                return
            
            len = 0
            zigzag(root, True)
            max_len = max(max_len,len - 1)

            len = 0
            zigzag(root, False)
            max_len = max(max_len,len - 1)

            if root.left:
                call(root.left)
            if root.right:
                call(root.right)
        
        call(root)

        return max_len

        #one way to optimize is to stop at leaf nodes, not no nodes

        #fresh thinking:
            #maybe we can optimize it by not calling it for every node
