# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        elif(root.left==None and root.right==None):
            return 1
        depth1=0
        depth2=0
        if(root.left==None):
            depth2=1+self.maxDepth(root.right)
        elif(root.right==None):
            depth1=1+self.maxDepth(root.left)
        else:
            depth1=1+self.maxDepth(root.left)
            depth2=1+self.maxDepth(root.right)
        return max(depth1,depth2)