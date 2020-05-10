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

# Solution 1, double recursion, no efficient
class Solution:
    def dfs(self, l, t):
        if l is None:
            return True
        if t is None:
            return False
        
        return l.val == t.val and (self.dfs(l.next, t.left) or self.dfs(l.next, t.right))

        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return head is None
        
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)