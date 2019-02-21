class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res = []
        curr = sum(c for c in A if c % 2 == 0)
        
        for val, idx in queries:
            if A[idx] % 2 == 0:
                curr -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                curr += A[idx]
            res.append(curr)
        return res
