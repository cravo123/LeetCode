class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** 0.5)
        
        while W > 1:
            if area % W == 0:
                break
            W -= 1
        return [area // W, W]