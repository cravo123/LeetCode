import math, random

# Solution 1, rejection-sampling
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            i = random.uniform(-1, 1) * self.r
            j = random.uniform(-1, 1) * self.r
            if i * i + j * j <= self.r * self.r:
                return [i + self.x, j + self.y]

# Solution 2, polar coordinates
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r_t = math.pow(random.random(), 0.5) * self.r
        theta = random.random() * math.pi * 2
        
        i = self.x + r_t * math.cos(theta)
        j = self.y + r_t * math.sin(theta)
        
        return [i, j]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()