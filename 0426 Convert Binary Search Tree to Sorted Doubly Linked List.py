"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

# Solution 1, recursion, similar to recursion version of
# reversing a linked list. We return head and tail at the 
# same time.
class Solution:
    def dfs(self, node):
        if node is None:
            return None, None
        
        l_h, l_t = self.dfs(node.left)
        r_h, r_t = self.dfs(node.right)
        
        if l_t:
            head = l_h
            l_t.right = node
            node.left = l_t
        else:
            head = node
            node.left = None
        
        if r_h:
            tail = r_t
            node.right = r_h
            r_h.left = node
        else:
            tail = node
            node.right = None
        
        head.left = tail
        tail.right = head
        
        return head, tail
        
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        res, _ = self.dfs(root)
        
        return res

# Solution 2, in-order traversal
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = curr = None
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                if curr is None:
                    head = curr = p
                else:
                    curr.right = p
                    p.left = curr
                    curr = p
                p = p.right
        if head:
            head.left = curr
        if curr:
            curr.right = head
            
        return head
        