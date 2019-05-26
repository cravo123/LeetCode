# Solution 1, simulation
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)
        
        for _ in range(V):
            i = K
            
            # try to move left
            while i > 0 and heights[i] >= heights[i - 1]:
                i -= 1
            
            # if do move left
            if heights[i] < heights[K]:
                while heights[i] == heights[i + 1]:
                    i += 1
                heights[i] += 1
                continue
            
            # try to move right
            while i < n - 1 and heights[i] >= heights[i + 1]:
                i += 1
            
            # if do move right
            if heights[i] < heights[K]:
                while heights[i] == heights[i - 1]:
                    i -= 1
                heights[i] += 1
                continue
            
            heights[K] += 1
        
        return heights

# Solution 1.1, simulation, DRY
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)
        
        for _ in range(V):
            for di in [-1, 1]:
                i = K
                while 0 <= i + di < n and heights[i] >= heights[i + di]: # got-cha
                    i += di
                if heights[i] != heights[K]:
                    while heights[i] == heights[i - di]:
                        i -= di
                    heights[i] += 1
                    break 
            else:
                heights[K] += 1
        
        return heights

# Solution 1.2, simulation, elegant but not very intuitive
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)
        
        for _ in range(V):
            curr = K
            
            # move left
            while curr > 0 and heights[curr] >= heights[curr - 1]:
                curr -= 1
            
            # bottom might be flat, so move right
            while curr < n - 1 and heights[curr] >= heights[curr + 1]:
                curr += 1
            
            while curr > K and heights[curr] >= heights[curr - 1]:
                curr -= 1
            
            heights[curr] += 1
        
        return heights