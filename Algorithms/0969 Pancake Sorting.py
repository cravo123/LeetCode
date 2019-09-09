# Solution 1, not the fewest operation solution, but the most straight-forward one
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        n = len(A)
        curr = n
        
        while curr > 0:
            max_val = max(A[:curr])
            max_idx = A.index(max_val)
            
            res.append(max_idx + 1)
            A[0:(max_idx + 1)] = A[max_idx::-1]
            
            res.append(curr)
            A[0:curr] = A[(curr-1)::-1]
            
            curr -= 1
        
        return res

# Solution 1.1, same idea
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        
        n = len(A)
        
        for k in range(n, 0, -1):
            v = max(A[:k])
            idx = A.index(v)
            
            if k - 1 != idx:
                res.append(idx + 1)
                res.append(k)
                A = A[:(idx + 1)][::-1] + A[(idx + 1):]
                A = A[:k][::-1] + A[k:]
        
        return res