import string

# Solution 1, double-end BFS
class Solution:
    def change(self, word, d):
        res = []
        
        for i, c in enumerate(word):
            for x in string.ascii_lowercase:
                if x == c:
                    continue
                new_word = word[:i] + x + word[(i + 1):]
                if new_word in d:
                    res.append(new_word)
        
        return res
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = set(wordList)
        
        if endWord not in d:
            return 0
        
        left = set([beginWord])
        right = set([endWord])
        steps = 0
        
        seen = set()
        
        while left:
            tmp = set()
            steps += 1
            for word in left:
                if word in right:
                    return steps
                seen.add(word)
                for new_word in self.change(word, d):
                    if new_word not in seen:
                        tmp.add(new_word)
            left, right = right, tmp
            
        return 0

# Solution 1.1, without Seen set
class Solution:
    def change(self, word, d):
        res = []
        
        for i, c in enumerate(word):
            for x in string.ascii_lowercase:
                if x == c:
                    continue
                new_word = word[:i] + x + word[(i + 1):]
                if new_word in d:
                    res.append(new_word)
        
        return res
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = set(wordList)
        
        if endWord not in d:
            return 0
        
        left = set([beginWord])
        right = set([endWord])
        steps = 0
        
        while left:
            tmp = set()
            steps += 1
            for word in left:
                if word in right:
                    return steps
                d.discard(word)
                for new_word in self.change(word, d):
                    tmp.add(new_word)
            left, right = right, tmp
            
        return 0

# Solution 2, plain bfs
class Solution:
    def generate_next_words(self, curr, wordList, seen):
        res = []
        for word in curr:
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c != word[i]:
                        new_word = word[:i] + c + word[(i + 1):]
                        if new_word in wordList and new_word not in seen:
                            seen.add(new_word)
                            res.append(new_word)
        return res
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        curr = [beginWord]
        seen = set(curr)
        steps = 1
        
        while curr:
            if any(word == endWord for word in curr):
                return steps
            
            tmp = self.generate_next_words(curr, wordList, seen)
            
            steps += 1
            curr = tmp
        
        return 0