# Solution 1, simulation


# Solution 2, simulation, but not very intuitive
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