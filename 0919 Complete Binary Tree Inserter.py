import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, O(1) insert, O(n) build queue
# Save treenode to a deque
# pop from left all nodes that have both left and right children
# then the front-end of deque will be the parent where new node can be inserted
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = self._build_queue(root)        

    def insert(self, v: int) -> int:
        p = self.q[0]
        new_node = TreeNode(v)
        
        if p.left:
            p.right = new_node
            self.q.append(p.left)
            self.q.append(p.right)
            self.q.popleft()
        else:
            p.left = new_node
        
        return p.val

    def get_root(self) -> TreeNode:
        return self.root
    
    def _build_queue(self, root):
        q = collections.deque([root])
        
        while True:
            curr = q[0]
            if curr.left and curr.right:
                q.append(curr.left)
                q.append(curr.right)
                q.popleft()
            else:
                break
        return q
            


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()