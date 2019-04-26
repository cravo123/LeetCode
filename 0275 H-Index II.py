class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        
        i, j = 0, n - 1
        
        while i < j:
            m = (i + j) // 2
            
            v = citations[m]
            cnt = n - m
            
            if v < cnt:
                i = m + 1
            else:
                j = m
        return n - i if citations[i] >= n - i else 0