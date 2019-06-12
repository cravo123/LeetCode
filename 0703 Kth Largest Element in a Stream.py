import heapq

# Solution 1, priority queue
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.q = nums
        heapq.heapify(self.q)
        
        self.clean()
        
    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        self.clean()
        
        res = heapq.heappop(self.q)
        heapq.heappush(self.q, res)
        
        return res
    
    def clean(self):
        while len(self.q) > self.size:
            heapq.heappop(self.q)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)