class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        q = nums
        
        while q:
            tmp = []
            cnt = 0
            for c in q:
                if c & 1:
                    cnt += 1
                c //= 2
                if c:
                    tmp.append(c)
            q = tmp
            res += (n - cnt) * cnt
        
        return res