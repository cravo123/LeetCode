# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, DFS, and use hash-set to save seen values
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.seen = set()
        self._recover(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
    
    def _recover(self, curr, val):
        if curr is not None:
            curr.val = val
            self.seen.add(val)
            self._recover(curr.left, val * 2 + 1)
            self._recover(curr.right, val * 2 + 2)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)