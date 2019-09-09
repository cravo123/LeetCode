# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution:
    def dfs(self, cnt, base):
        if cnt == 0:
            yield None
        
        for i in range(cnt):
            L, R = i, cnt - i - 1
            for p in self.dfs(L, base):
                for q in self.dfs(R, i + 1 + base):
                    x = TreeNode(i + base)
                    x.left = p
                    x.right = q
                    yield x
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        res = [p for p in self.dfs(n, 1)]
        
        return res