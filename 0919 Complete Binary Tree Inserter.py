# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque([root])
        self._clean()

    def insert(self, v: int) -> int:
        self._clean()
        p = self.q.popleft()
        if p.left is None:
            p.left = TreeNode(v)
            self.q.append(p.left)
            self.q.appendleft(p)
        else:
            p.right = TreeNode(v)
            self.q.append(p.right)
        return p.val

    def get_root(self) -> TreeNode:
        return self.root
    
    def _clean(self):
        while self.q:
            p = self.q.popleft()
            
            for x in [p.left, p.right]:
                if x:
                    self.q.append(x)
            
            if not p.left or not p.right:
                self.q.appendleft(p)
                break                
    

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()