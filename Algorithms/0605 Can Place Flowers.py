# Solution 1, Greedy
# Actually this solution is elegant in a sense that we don't need to
# treat corner cases like( [0], [0, 0, 0]) specially
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        
        i = 0
        
        while i < m:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            
            if n <= 0:
                return True
            i += 1
        return False

# Solution 1.1, better implementation
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        
        for i, c in enumerate(flowerbed):
            if c == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            
            if n <= 0:
                return True
        return False