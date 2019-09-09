import collections

# Solution 1, precache eligible words
# Say we have 'abc', we will cache '*bc', 'a*c' and 'ab*' to represent
# replacing one char
# Note that it is a common trick to use '*' as a representive of changing 
# a char at a specific position to any other chars
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.Counter()
        self.word_list = set()
    
    def change_char(self, word):
        
        for i, c in enumerate(word):
            yield word[:i] + '*' + word[(i + 1):]
    
    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        
        for word in words:
            self.word_list.add(word)
            
            for t_word in self.change_char(word):
                self.d[t_word] += 1

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        
        if word not in self.word_list and any(new_word in self.d for new_word in self.change_char(word)):
            return True
        
        if word in self.word_list and any(self.d[new_word] > 1 for new_word in self.change_char(word)):
            return True
        
        return False


# Solution 2, 
# This question is pretty open, there are other ways to preprocess the data
# One is use word length as bucket to store all words
# t.b.c


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)