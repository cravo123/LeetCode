import collections, string

# Solution 1, BFS and cache previous node
# This problem actually requires BFS/DFS knowledge and also back-tracking
# when generating the paths
class Solution:
    def word_list(self, word, wordList):
        q = set()
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if c == word[i]:
                    continue
                tmp_word = word[:i] + c + word[(i + 1):]
                if tmp_word in wordList:
                    q.add(tmp_word)
        return q
    
    def dfs(self, curr_word, target, prev, path, res):
        if curr_word == target:
            res.append([curr_word] + path[::-1])
            return
        
        path.append(curr_word)
        for new_word in prev[curr_word]:
            self.dfs(new_word, target, prev, path, res)
        path.pop()
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        prev = collections.defaultdict(set)
        
        curr = set([beginWord])
        
        while curr:
            tmp = set()
            
            if endWord in curr:
                break
            
            for word in curr:
                for new_word in self.word_list(word, wordList):
                    tmp.add(new_word)
                    prev[new_word].add(word)
            
            curr = tmp
            wordList -= curr
        
        if endWord not in prev:
            return []
        
        path = []
        res = []
        self.dfs(endWord, beginWord, prev, path, res)
        
        return res
    
        

# Solution 2, complex 
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
    
        