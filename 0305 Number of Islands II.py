# Solution 1, Union-Find
class Solution:
    def find(self, i, j, m, n, d):
        # Find all idx
        res = set()
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and (x, y) in d:
                res.add(d[x, y])
        
        return res
    
    def find_parent(self, idx, parents):
        if parents[idx] != idx:
            parents[idx] = self.find_parent(parents[idx], parents)
        return parents[idx]
    
    def union(self, curr_parents, parents):
        curr_parents = set(curr_parents)
        x = curr_parents.pop()
        v = self.find_parent(x, parents)
        
        for y in curr_parents:
            parents[y] = v
    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        cnt = 0
        d = {} # position -> idx
        parents = {}
        res = []
        total = 0
        
        for i, j in positions:
            curr = self.find(i, j, m, n, d)
            curr_parents = set(self.find_parent(x, parents) for x in curr)
            
            length = len(curr_parents)
            
            if length == 0:
                d[i, j] = cnt
                parents[cnt] = cnt
                cnt += 1
                total += 1
            else:
                total -= length - 1
                self.union(curr_parents, parents)
                d[i, j] = self.find_parent(curr_parents.pop(), parents)
            res.append(total)
        return res

# Solution 2, Union-Find elegant solution
# Notice that in Solution 1, Union-Find logic could be extracted as a separate class
