# Solution 1, simulation
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        q = collections.Counter(arr)
        n = len(arr)
        
        q = [cnt for _, cnt in q.items()]
        q.sort(reverse=True)
        
        curr = 0
        cnt = 0
        while curr < n / 2:
            curr += q[cnt]
            cnt += 1
        
        return cnt