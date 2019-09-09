import random

class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.d = {} # used -> unused
        self.cap = self.n_rows * self.n_cols

    def flip(self) -> List[int]:
        v = random.randrange(self.cap)
        self.cap -= 1
        v1 = self.d.get(v, v)
        self.d[v] = self.d.get(self.cap, self.cap) # gotcha
        
        i, j = divmod(v1, self.n_cols)
        return [i, j]

    def reset(self) -> None:
        self.d = {}
        self.cap = self.n_rows * self.n_cols

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()