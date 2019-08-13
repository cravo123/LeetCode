import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1, simulation using hashmap
class Solution:
    def dfs(self, node, seen):
        if node is None:
            return
        seen[node.val] += 1
        
        self.dfs(node.left, seen)
        self.dfs(node.right, seen)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        seen = collections.Counter()
        
        self.dfs(root, seen)
        
        val = max(seen.values())
        res = [c for c in seen if seen[c] == val]
        
        return res

# Solution 2, recursion, returning two values trick
# O(1) memory solution if we ignore call stack space
class Solution:
    def dfs(self, node, prev_val, prev_cnt):
        if node is None:
            return prev_val, prev_cnt
        
        prev_val, prev_cnt = self.dfs(node.left, prev_val, prev_cnt)
        
        if prev_val == node.val:
            prev_cnt += 1
        else:
            prev_val, prev_cnt = node.val, 1
        
        if prev_cnt == self.res_cnt:
            self.res_vals.append(prev_val)
        elif prev_cnt > self.res_cnt:
            self.res_cnt = prev_cnt
            self.res_vals = [prev_val]
        
        return self.dfs(node.right, prev_val, prev_cnt)
        
    def findMode(self, root: TreeNode) -> List[int]:
        self.res_cnt = 0
        self.res_vals = []
        
        self.dfs(root, None, 0)
        
        return self.res_vals