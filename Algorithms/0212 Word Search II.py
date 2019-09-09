import collections

# Solution 1, Trie + DFS
class Node:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0
        
    def add_word(self, word):
        p = self.root
        
        for c in word:
            p = p.children[c]
        
        if not p.is_word:
            p.is_word = True
            self.size += 1
    
    def get_size(self):
        return self.size
    
    def get_root(self):
        return self.root

class Solution:
    def dfs(self, i, j, p, board, m, n, path, res):
        c = board[i][j]
        if c not in p.children:
            return
        
        path.append(c)
        p = p.children[c]
        if p.is_word:
            p.is_word = False
            res.append(''.join(path))
        
        board[i][j] = '#'
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n:
                self.dfs(x, y, p, board, m, n, path, res)
        board[i][j] = c
        path.pop()
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        m, n = len(board), len(board[0]) if board else 0
        res = []
        path = []
        for i in range(m):
            for j in range(n):
                p = trie.get_root()
                self.dfs(i, j, p, board, m, n, path, res)
                
        return res

# Solution 2, brute force DFS (TLE)
class Solution:
    def dfs(self, idx, word, board, i, j, m, n):
        if word[idx] != board[i][j]:
            return False
        
        if idx + 1 == len(word):
            return True
        
        board[i][j] = '#'
        
        flag = False
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and self.dfs(idx + 1, word, board, x, y, m, n):
                flag = True
                break
                
        board[i][j] = word[idx]
        return flag
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0]) if board else 0
        
        res = []
        for word in words:
            flag = False
            for i in range(m):
                for j in range(n):
                    if self.dfs(0, word, board, i, j, m, n):
                        res.append(word)
                        flag = True
                    if flag:
                        break
                if flag:
                    break
        return res