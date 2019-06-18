import collections

# Solution 1, simulation
# count each edge
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = collections.Counter()
        
        for row in wall:
            curr = 0
            for width in row[:-1]:
                curr += width
                d[curr] += 1
        
        if d:
            return len(wall) - d.most_common(1)[0][1]
        return len(wall)