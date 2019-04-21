import collections, string

# Solution 1, complex 
class Solution:
    def change(self, word):
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if c == word[i]:
                    continue
                yield word[:i] + c + word[(i + 1):]
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_list = set(wordList)
        
        if endWord not in word_list:
            return []
        
        d = collections.defaultdict(set)
        
        q = [beginWord]
        seen = set()
        seen.add(beginWord)
        flag = False
        steps = 1
        while q:
            t = []
            
            for word in q:
                if word == endWord:
                    flag = True
                for new_word in self.change(word):
                    if new_word in word_list:
                        d[new_word].add(word)
                        if new_word not in seen:
                            t.append(new_word)
                            seen.add(new_word)
            if flag:
                break
            q = t
            steps += 1
        
        if not flag:
            return []
        
        res = self.generate(endWord, beginWord, d, steps)
        
        return res
    
    def dfs(self, start, end, d, path, res, seen, steps):
        if len(path) >= steps:
            return
        if start == end:
            path.append(start)
            res.append(path[::-1])
            path.pop()
            return
        
        path.append(start)
        seen.add(start)
        for next_word in d[start]:
            if next_word not in seen:
                self.dfs(next_word, end, d, path, res, seen, steps)
        path.pop()
        seen.discard(start)
    
    def generate(self, start, end, d, steps):
        path = []
        res = []
        seen = set()
        
        self.dfs(start, end, d, path, res, seen, steps)
        
        return res
    
        