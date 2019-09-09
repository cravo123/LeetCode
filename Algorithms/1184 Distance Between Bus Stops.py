# Solution 1, simulation
# Minimum distance is either clockwise or counterclockwise
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        
        curr = sum(distance[start:destination])
        
        return min(curr, sum(distance) - curr)