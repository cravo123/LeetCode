# Solution 1,
# Tricky point is to early stop and prune
# Since maze is 1 million rows and cols, it is impossible to 
# enumerate all results using bfs(memory limit) or dfs(recursion limit)
# But since blocked has a length, we can proof that blocked can only cover 
# an area with len(blocked) - 1 steps away from source(this is a very loose constraint)
class Solution(object):
    def check(self, source, target, blocked):
        limit = int(1e6)
        
        steps = 0
        
        curr = [source]
        target = tuple(target)
        seen = set(tuple(source))
        for x in blocked:
            seen.add(tuple(x))
        
        while curr and steps < len(blocked):
            tmp = []
            
            for x, y in curr:
                if (x, y) == target:
                    return True
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    i, j = x + dx, y + dy
                    if 0 <= i < limit and 0 <= j < limit and (i, j) not in seen:
                        seen.add((i, j))
                        tmp.append((i, j))
            curr = tmp
            steps += 1
        
        return False if not curr else True 
        
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        
        return self.check(source, target, blocked) and self.check(target, source, blocked)