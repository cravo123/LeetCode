"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

# Solution 1, grid search, same as LC 0240
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = y = 1
        while y < 1000 and customfunction.f(x, y) < z:
            y *= 2
        
        res = []
        while x > 0 and y > 0:
            val = customfunction.f(x, y)
            if val > z:
                y -= 1
            elif val < z:
                x += 1
            else:
                res.append([x, y])
                x += 1
        
        return res