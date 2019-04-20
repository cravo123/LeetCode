# Solution 1, back-tracking with caching
# First thought we may need "turn" as a flag, but turn info is
# already stored in "used" list, like odd or even of True in "used"
class Solution:
    def dfs(self, curr, total, used, d, turn):
        x = tuple(used)
        if (turn, x) in d:
            return d[turn, x]
        
        if curr >= total:
            return False
        
        for i in range(len(used)):
            if used[i] == False:
                used[i] = True
                if not self.dfs(curr + i + 1, total, used, d, 1 - turn):
                    used[i] = False
                    d[turn, tuple(used)] = True
                    return True
                used[i] = False
        d[turn, tuple(used)] = False
        
        return False
        
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        if sum(i + 1 for i in range(maxChoosableInteger)) < desiredTotal:
            return False
        
        used = [False for i in range(maxChoosableInteger)]
        d = {}
        return self.dfs(0, desiredTotal, used, d, 0)

# Solution 1.1 optimized Solution 1
# i.e. we don't need "turn" to mark player's turn
class Solution:
    def dfs(self, curr, total, used, d):
        x = tuple(used)
        if x in d:
            return d[x]
        
        if curr >= total:
            return False
        
        for i in range(len(used)):
            if used[i] == False:
                used[i] = True
                if not self.dfs(curr + i + 1, total, used, d):
                    used[i] = False
                    d[tuple(used)] = True
                    return True
                used[i] = False
        d[tuple(used)] = False
        
        return False
        
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        if sum(i + 1 for i in range(maxChoosableInteger)) < desiredTotal:
            return False
        
        used = [False for i in range(maxChoosableInteger)]
        d = {}
        return self.dfs(0, desiredTotal, used, d)


# Solution 2, better solution
class Solution:
    def dfs(self, curr, total, used, d):
        if tuple(used) in d:
            return d[tuple(used)]
        
        if any(curr + i + 1 >= total for i in range(len(used)) if used[i] == False):
            d[tuple(used)] = True
            return True
        
        for i in range(len(used)):
            if used[i] == False:
                used[i] = True
                if not self.dfs(curr + i + 1, total, used, d):
                    used[i] = False
                    d[tuple(used)] = True
                    return True
                used[i] = False
        d[tuple(used)] = False
        
        return False
        
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger < 2 * desiredTotal:
            return False
        
        used = [False for _ in range(maxChoosableInteger)]
        d = {}
        
        return self.dfs(0, desiredTotal, used, d)
        