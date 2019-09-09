# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1, Sorting
class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        q = A + B
        q.sort(key=lambda x: x.start)
        
        res = []
        prev_end = float('-inf')
        
        for interval in q:
            if prev_end >= interval.start:
                res.append(Interval(interval.start, min(prev_end, interval.end)))
            prev_end = max(prev_end, interval.end)
        
        return res

# Solution 2, "merge-sort" like
class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        res = []
        i = j = 0
        m, n = map(len, (A, B))
        
        while i < m and j < n:
            if A[i].end < B[j].start:
                i += 1
            elif B[j].end < A[i].start:
                j += 1
            else:
                res.append(Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end)))
                if A[i].end <= B[j].end:
                    i += 1
                else:
                    j += 1

        return res

# Solution 3, more simple
class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        res = []
        i = j = 0
        m, n = map(len, (A, B))
        
        while i < m and j < n:
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            
            if lo <= hi: # This is an elegant solution
                res.append(Interval(lo, hi))
            
            if A[i].end <= B[j].end:
                i += 1
            else:
                j += 1
        
        return res