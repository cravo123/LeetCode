# Solution 1, Union Find
# Find it is easier to understand if we abstract Union Find logic
# and create a separate data structure class for it.

class UFS: # Union Find Set
    def __init__(self, n):
        self.size = n
        self.parents = [i for i in range(n)]
    
    def find_parent(self, idx):
        if idx != self.parents[idx]:
            self.parents[idx] = self.find_parent(self.parents[idx])
        return self.parents[idx]
    
    def union(self, i, j):
        p_i, p_j = map(self.find_parent, (i, j))
        if p_i != p_j:
            self.parents[p_i] = p_j
            self.size -= 1
        
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        uf = UFS(N)
        
        for t, i, j in sorted(logs):
            uf.union(i, j)
            
            if uf.size == 1:
                return t
        
        return -1