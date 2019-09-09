# Solution 1, greedy
# Intuition is that, instead of chasing you around the map, 
# ghost can go to target, and wait for you. This is an optimial strategy
# because sum of two edges of a triangle is larger than the third one.
class Solution:
    def dist(self, curr, target):
        return abs(curr[0] - target[0]) + abs(curr[1] - target[1])
    
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        curr = self.dist([0, 0], target)
        if any(self.dist(ghost, target) <= curr for ghost in ghosts):
            return False
        return True