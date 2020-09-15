# Question: 237. Remove Node from Linked List 

# Attempts: 1
# Completed: Y 
# Optimal: Y

# Time: O(n)
# Space: O(1)

# Problems Encountered: None 

# Other Solutions:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val; 
        node.next = node.next.next 
    
