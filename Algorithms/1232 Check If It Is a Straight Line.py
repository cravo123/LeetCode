# Solution 1, simulation
# Use multiplication form of slope calculation
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x, y = coordinates[0]
        a, b = coordinates[1][0] - x, coordinates[1][1] - y
        
        for i in range(2, len(coordinates)):
            if a * (coordinates[i][1] - y) != b * (coordinates[i][0] - x):
                return False
        
        return True