# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def halve_list(self, node):
        prev, slow, fast = None, node, node
        
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        
        return node, slow
    
    def dfs(self, node):
        if node is None:
            return
        
        if node.next is None:
            return TreeNode(node.val)
        
        first, second = self.halve_list(node)
        root = TreeNode(second.val)
        root.left = self.dfs(first)
        root.right = self.dfs(second.next)
        
        return root
        
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        res = self.dfs(head)
        
        return res