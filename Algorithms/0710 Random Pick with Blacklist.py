import random
# Solution 1, naive pick
class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.bl = set(blacklist)
        self.N = N

    def pick(self) -> int:
        while True:
            v = random.randrange(0, self.N)
            if v not in self.bl:
                return v

# Solution 2, more elegant solution
class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)
        self.N = N - len(blacklist)
        self.d = {}
        
        right = N - 1
        
        for c in blacklist:
            if c < self.N:
                while right in blacklist:
                    right -= 1
                self.d[c] = right
                right -= 1

    def pick(self) -> int:
        v = random.randrange(0, self.N)
        
        return v if v not in self.d else self.d[v]


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()