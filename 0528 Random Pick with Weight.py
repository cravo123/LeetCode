import bisect
import random

class Solution:
    def __init__(self, w: List[int]):
        self.cum_sum = []
        curr = 0
        for c in w:
            curr += c
            self.cum_sum.append(curr)
        
        self.max_val = self.cum_sum[-1]

    def pickIndex(self) -> int:
        v = random.randrange(1, self.max_val + 1)
        idx = bisect.bisect_left(self.cum_sum, v)
        
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()