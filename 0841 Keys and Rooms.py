# Solution 1, BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in rooms]
        
        q = [0]
        seen[0] = True
        
        while q:
            tmp = []
            for idx in q:
                for key in rooms[idx]:
                    if not seen[key]:
                        tmp.append(key)
                        seen[key] = True
            q = tmp
        
        return len(rooms) == sum(seen)

# Solution 2, DFS, iterative
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in rooms]
        
        q = [0]
        seen[0] = True
        
        while q:
            idx = q.pop()
            
            for key in rooms[idx]:
                if not seen[key]:
                    q.append(key)
                    seen[key] = True
        
        return len(rooms) == sum(seen)

# Solution 3, DFS Recursive
class Solution:
    def dfs(self, idx, rooms, seen):
        seen[idx] = True
        
        for key in rooms[idx]:
            if not seen[key]:
                self.dfs(key, rooms, seen)
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in rooms]
        
        self.dfs(0, rooms, seen)
        
        return len(rooms) == sum(seen)

# Solution 4, Union Find
class Solution:
    def parent(self, idx, d):
        if idx != d[idx]:
            d[idx] = self.parent(d[idx], d)
        return d[idx]
            
    def dfs(self, idx, rooms, d):
        p_idx = self.parent(idx, d)
        
        for key in rooms[idx]:
            p_key = self.parent(key, d)
            if p_key != p_idx:
                d[key] = p_idx
                self.dfs(key, rooms, d)
        
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = {i:i for i in range(len(rooms))}
        
        self.dfs(0, rooms, d)
        
        parents = set(d[i] for i in range(len(rooms)))
        
        return len(parents) == 1