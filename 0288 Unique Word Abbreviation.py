import collections

# Note definition of 'unique'.
class ValidWordAbbr:
    def change(self, word):
        if len(word) <= 2:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]
        
    def __init__(self, dictionary: List[str]):
        self.d = collections.defaultdict(set)
        
        for word in dictionary:
            self.d[self.change(word)].add(word)

    def isUnique(self, word: str) -> bool:
        v = self.change(word)
        return v not in self.d or word in self.d[v] and len(self.d[v]) == 1


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)