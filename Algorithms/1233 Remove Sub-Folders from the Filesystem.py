import collections

# Solution 1, Greedy
# After sorting folder, parent folder will definitely appear before subfolders
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        q = []
        
        for f in folder:
            if len(q) == 0 or not f.startswith(q[-1]) or not f.startswith(q[-1] + '/'):
                q.append(f)
        
        return q

# Solution 2, Union-Find
class Node:
    def __init__(self):
        self.is_path = False
        self.subpaths = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_path(self, path):
        path = path.split('/')
        
        curr = self.root
        
        for p in path:
            if curr.subpaths[p].is_path:
                return
            curr = curr.subpaths[p]
        curr.is_path = True
    
    def dfs(self, curr, path, res):
        if curr is None or curr.is_path:
            res.append('/'.join(path))
            return
        
        for p, v in curr.subpaths.items():
            path.append(p)
            self.dfs(v, path, res)
            path.pop()
            
    
    def generate_paths(self):
        res = []
        path = []
        curr = self.root
        
        self.dfs(curr, path, res)
        
        return res
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        
        for f in folder:
            t.add_path(f)
        
        return t.generate_paths()