from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.q = nums
        heapify(self.q)
        
        while len(self.q) > self.size:
            heappop(self.q)

    def add(self, val: int) -> int:
        heappush(self.q, val)
        
        if len(self.q) > self.size:
            heappop(self.q)
        
        res = heappop(self.q)
        heappush(self.q, res)
        
        return res