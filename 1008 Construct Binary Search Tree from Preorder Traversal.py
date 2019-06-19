import bisect
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, preorder, left, right):
        if left > right:
            return
        res = TreeNode(preorder[left])
        idx = bisect.bisect_left(preorder, preorder[left], lo=left + 1)
        
        res.left = self.dfs(preorder, left + 1, idx - 1)
        res.right = self.dfs(preorder, idx, right)
        
        return res
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.dfs(preorder, 0, len(preorder) - 1)

# Solution 2, iteration
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        res = TreeNode(preorder[0])
        
        q = [res]
        
        for i in range(1, len(preorder)):
            tmp = TreeNode(preorder[i])
            if q[-1].val > preorder[i]:
                q[-1].left = tmp
                q.append(tmp)
            else:
                while q and q[-1].val < preorder[i]:
                    prev = q.pop()  
                prev.right = tmp
                q.append(tmp)
        
        return res