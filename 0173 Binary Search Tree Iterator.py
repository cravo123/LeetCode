# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, iteratively in-order traverse a tree
class BSTIterator:
    def __init__(self, root):
        self.q = []
        self.push(root)
        
    def push(self, node):
        while node:
            self.q.append(node)
            node = node.left
    
    def next(self):
        """
        @return the next smallest number
        """
        node = self.q.pop()
        res = node.val
        
        p = node.right
        self.push(p)
        
        return res

# Solution 2, Flatten BST to array, then iterate
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.idx = 0
        self.q = []
        self.dfs(root)
    
    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        self.q.append(node.val)
        self.dfs(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.q[self.idx]
        self.idx += 1
        
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        
        return self.idx < len(self.q)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()