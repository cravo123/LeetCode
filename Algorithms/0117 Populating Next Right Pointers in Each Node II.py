"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Solution 1, O(W) space where W is the width of tree
# Level Traversal, eay to understand
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        curr = [root]
        
        while curr:
            tmp = [x for p in curr for x in [p.left, p.right] if x]
            
            for i in range(len(tmp) - 1):
                tmp[i].next = tmp[i + 1]
            
            curr = tmp
        return root

# Solution 2, O(1) space
# Level-order traversal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        
        while curr:
            dummy = runner = Node(None, None, None, None)
            
            while curr:
                if curr.left:
                    runner.next = curr.left
                    runner = runner.next
                if curr.right:
                    runner.next = curr.right
                    runner = runner.next
                curr = curr.next
            #runner.next = None
            curr = dummy.next # got-cha
        return root

# Solution 2.1, better implementation
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        dummy = runner = Node(None, None, None, None)
        
        while curr:
            runner.next = curr.left
            if runner.next:
                runner = runner.next
            
            runner.next = curr.right
            if runner.next:
                runner = runner.next
            
            curr = curr.next
            
            if not curr:
                curr = dummy.next
                runner = dummy
        
        return root