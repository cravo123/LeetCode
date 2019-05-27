import collections

# Solution 1,

# Solution 2, brute-force caching all prefix and suffix combinations
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = collections.defaultdict(set)
        self.suffix = collections.defaultdict(set)
        self.weights = {word:i for i, word in enumerate(words)}
        
        for word in words:
            for i in range(len(word) + 1):
                self.prefix[word[:i]].add(word)
                self.suffix[word[i:]].add(word)
        
    def f(self, prefix: str, suffix: str) -> int:
        cans = self.prefix[prefix] & self.suffix[suffix]
        
        if not cans:
            return -1
        return max(self.weights[word] for word in cans)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)