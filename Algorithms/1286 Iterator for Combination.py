# Solution 1, brute-force, O(n ^ k), here k = combinationLength
# DFS to calculate all paths first
# This is not a good solution
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = []
        self.idx = 0
        self.path = []
        self.chars = characters
        self.max_len = combinationLength
        
        self.dfs(0)

    def next(self) -> str:
        self.idx += 1
        return self.res[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.res)
    
    def dfs(self, idx):
        if len(self.path) == self.max_len:
            self.res.append(''.join(self.path))
            return
        
        for i in range(idx, len(self.chars)):
            self.path.append(self.chars[i])
            self.dfs(i + 1)
            self.path.pop()

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()