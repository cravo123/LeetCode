# Solution 1, elegant one
# it is more testing your modeling ability. Was thinking different kinds of two-pointer
# solution in the contest, but it is actually group (A[i] and i) together, and mark its
# highest values seen so far
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = curr = float('-inf')
        
        for i, c in enumerate(A):
            res = max(res, curr + c - i)
            curr = max(curr, c + i)
        
        return res