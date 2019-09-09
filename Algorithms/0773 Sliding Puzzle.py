from heapq import *

# Solution 1, Breadth-First-Search
class Solution:
    def moves(self, curr):
        curr = list(curr)
        i = curr.index(0)
        
        for di in [-1, 1, -3, 3]:
            x = i + di
            if x < 0 or x >= 6:
                continue
            if i == 2 and di == 1:
                continue
            if i == 3 and di == -1:
                continue
            t = curr[::]
            t[i], t[x] = t[x], t[i]
            yield tuple(t)
            
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = tuple([1, 2, 3, 4, 5, 0])
        
        curr = tuple(board[0] + board[1])
        q = [curr]
        seen = set()
        seen.add(curr)
        steps = 0
        
        while q:
            tmp = []
            
            for x in q:
                if x == target:
                    return steps
                for y in self.moves(x):
                    if y not in seen:
                        tmp.append(y)
                        seen.add(y)
            q = tmp
            steps += 1
        return -1

# Solution 2, Best-First-Search, using priority queue
class Solution:
    def moves(self, curr):
        curr = list(curr)
        i = curr.index(0)
        
        for di in [-1, 1, -3, 3]:
            x = i + di
            if x < 0 or x >= 6:
                continue
            if i == 2 and di == 1:
                continue
            if i == 3 and di == -1:
                continue
            t = curr[::]
            t[i], t[x] = t[x], t[i]
            yield tuple(t)
            
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = tuple([1, 2, 3, 4, 5, 0])
        
        curr = tuple(board[0] + board[1])
        q = [[0, curr]]
        seen = set()
        seen.add(curr)
        
        while q:
            steps, x = heappop(q)
            
            if x == target:
                return steps
            
            for y in self.moves(x):
                if y not in seen:
                    heappush(q, [steps + 1, y])
                    seen.add(y)
        return -1