import string
# Solution 1, Trie

# Solution 2, DFS
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d.add(word)
    
    def dfs(self, idx, path, word):
        if idx == len(word):
            return ''.join(path) in self.d
        
        if word[idx] != '.':
            path.append(word[idx])
            res = self.dfs(idx + 1, path, word)
            path.pop()
            return res
        else:
            for c in string.ascii_lowercase:
                path.append(c)
                if self.dfs(idx + 1, path, word):
                    path.pop()
                    return True
                path.pop()
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        path = []
        return self.dfs(0, path, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)