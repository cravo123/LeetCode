# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, N, d):
        if N in d:
            return d[N]
        
        if N == 1:
            d[N].append(TreeNode(0))
            return d[N]
        
        for i in range(1, N - 1, 2):
            L, R = i, N - 1 - i
            if (L - R) % 2 == 0:
                for left_node in self.dfs(L, d):
                    for right_node in self.dfs(R, d):
                        root = TreeNode(0)
                        root.left = left_node
                        root.right = right_node
                        d[N].append(root)
        
        return d[N]
        
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        d = collections.defaultdict(list)
        d[0].append(None)
        
        self.dfs(N, d)
        
        return d[N]