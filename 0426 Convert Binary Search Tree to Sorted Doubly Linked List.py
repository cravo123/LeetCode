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
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if L[0] is None and R[0] is None:
            node.left = None
            node.right = None
            return node, node
        
        if L[0] is None:
            node.left = None
            node.right = R[0]
            R[0].left = node
            
            return node, R[1]
        if R[0] is None:
            L[1].right = node
            node.left = L[1]
            
            return L[0], node
        
        L[1].right = node
        node.left = L[1]
        node.right = R[0]
        R[0].left = node
        
        return L[0], R[1]
        
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head, tail = self.dfs(root)
        
        if head is None or tail is None:
            return head
        
        head.left = tail
        tail.right = head
        
        return head

# Solution 2, in-order traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
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
        