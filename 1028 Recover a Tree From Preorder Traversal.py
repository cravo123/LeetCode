# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        q = []
        n = len(S)
        
        i = 0
        
        while i < n:
            cnt = 0
            while i < n and S[i] == '-':
                cnt += 1
                i += 1
            
            val = 0
            while i < n and S[i].isdigit():
                val = val * 10 + int(S[i])
                i += 1
            
            t = TreeNode(val)
            while q and q[-1][1] >= cnt:
                q.pop()
            
            if q:
                if q[-1][0].left:
                    q[-1][0].right = t
                else:
                    q[-1][0].left = t
            q.append([t, cnt])
        
        return q[0][0]