# Solution 1, BFS
class Solution(object):
    def word_list(self, word, A):
        q = []
        
        for new_word in A:
            cnt = 0
            for i in range(len(word)):
                if word[i] != new_word[i]:
                    cnt += 1
                if cnt > 2:
                    break
            if cnt == 2:
                q.append(new_word)
        return q
        
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = set(A)
        
        res = 0
        
        while A:
            curr = [A.pop()]
            res += 1
            # BFS each group
            while curr:
                word = curr.pop()
                new_words = self.word_list(word, A)
                curr.extend(new_words)
                A -= set(new_words)
        return res

# Solution 1.1 BFS recursion
class Solution(object):
    def word_list(self, word, A):
        q = set()
        for new_word in A:
            cnt = 0
            for i in range(len(word)):
                if word[i] != new_word[i]:
                    cnt += 1
                if cnt > 2:
                    break
            if cnt == 2:
                q.add(new_word)
        return q
    
    def bfs(self, curr, A):
        if not curr:
            return
        
        word = curr.pop()
        new_words = self.word_list(word, A)
        A -= new_words
        
        curr |= new_words
        self.bfs(curr, A)
        
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = set(A)
        
        res = 0
        
        while A:
            curr = set([A.pop()])
            res += 1
            # remove similar string group layer by layer
            self.bfs(curr, A)
        
        return res

# Solution 2, Union-Find, TLE
# Create a UFS(Union Find Set) class so that we could delegate union-find
# logic completely. Makes code cleaner.
class UFS:
    def __init__(self):
        self.d = {} # word -> idx
        self.parents = {} # idx -> parent_idx
        self.idx = 0
        self.size = 0
    
    def add_word(self, word):
        if word not in self.d:
            self.d[word] = self.idx
            self.parents[self.idx] = self.idx
            self.idx += 1
            self.size += 1
    
    def dfs(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.dfs(self.parents[i])
        return self.parents[i]
    
    def find_parent(self, word):
        i = self.d[word]
        self.parents[i] = self.dfs(i)
        
        return self.parents[i]
    
    def union(self, word1, word2):
        p_1, p_2 = self.find_parent(word1), self.find_parent(word2)
        if p_1 != p_2:
            self.parents[p_1] = p_2
            self.size -= 1
    
    def find_size(self):
        return self.size

class Solution:
    def similar(self, word1, word2):
        cnt = sum(1 if a != b else 0 for a, b in zip(word1, word2))
        return cnt == 2
        
    def numSimilarGroups(self, A: List[str]) -> int:
        ufs = UFS()
        
        for i in range(len(A)):
            ufs.add_word(A[i])
            for j in range(i):
                if self.similar(A[i], A[j]):
                    ufs.union(A[i], A[j])
        
        return ufs.find_size()
                    
        