import collections

# Solution 1, Trie, prefix and suffix trie
class Node:
    def __init__(self):
        self.weight = set()
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word, weight):
        curr = self.root
        curr.weight.add(weight)
        
        for c in word:
            curr = curr.children[c]
            curr.weight.add(weight)
    
    def find_weight(self, word):
        curr = self.root
        if not curr.weight:
            return set()
        for c in word:
            curr = curr.children[c]
            if not curr.weight:
                return set()
        return curr.weight
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()
        
        for weight, word in enumerate(words):
            self.prefix.add_word(word, weight)
            self.suffix.add_word(reversed(word), weight)

    def f(self, prefix: str, suffix: str) -> int:
        v_prefix = self.prefix.find_weight(prefix)
        v_suffix = self.suffix.find_weight(reversed(suffix))
        
        if not v_prefix or not v_suffix:
            return -1
        
        return max(v_prefix & v_suffix)

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

# Solution 2.1, caching using only one dict
# key is prefix + '# + suffix, could use tuple as key also
class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        
        for i, word in enumerate(words):
            for left in range(len(word) + 1):
                for right in range(len(word), -1, -1):
                    self.d[word[:left] + '#' + word[right:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        tmp = prefix + '#' + suffix
        
        return self.d.get(tmp, -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)