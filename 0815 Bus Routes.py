import collections

# Solution 1, BFS
# Key is to find how to generate next stop
class Solution(object):
    def next_stops(self, curr, d, stops):
        buses = stops[curr]
        
        res = set()
        for c in buses:
            res |= d[c]
        return res
        
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        d = {i:set(c) for i, c in enumerate(routes)} # bus: stops
        
        stops = collections.defaultdict(set) # stop: buses
        
        for i, c in enumerate(routes):
            for stop in c:
                stops[stop].add(i)
        
        curr = [[S, 0]]
        seen = set([S])
        
        while curr:
            tmp = []
            
            for s, steps in curr:
                if s == T:
                    return steps
                for x in self.next_stops(s, d, stops):
                    if x not in seen:
                        tmp.append([x, steps + 1])
                        seen.add(x)
            curr = tmp
        return -1

# Solution 2, similar idea as Solution 1
# But we add route_i to the Seen set as this is much faster
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        buses = collections.defaultdict(set) # bus stop -> route
        
        for i, cs in enumerate(routes):
            for c in cs:
                buses[c].add(i)
        
        curr = [S]
        seen = set()
        
        steps = 0
        while curr:
            tmp = []
            
            for s in curr:
                if s == T:
                    return steps
                for route_i in buses[s]:
                    if route_i not in seen:
                        seen.add(route_i)
                        for next_stop in routes[route_i]:
                            tmp.append(next_stop)
            curr = tmp
            steps += 1
        return -1