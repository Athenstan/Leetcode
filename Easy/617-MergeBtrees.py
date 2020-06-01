# Question: 617. Merge Two Binary Trees

# Attempts: 1
# Completed: Y 
# Optimal: Y

# Time: 
# Space:

# Problems Encountered:

# Other Solutions:







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t2:
            return t1
        elif not t1:
            return t2
        else:
            if t1 and t2:
                t1.val+=t2.val
                t1.left=self.mergeTrees(t1.left,t2.left)
                t1.right=self.mergeTrees(t1.right,t2.right)
        return t1