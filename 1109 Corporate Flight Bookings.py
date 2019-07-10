# Solution 1, sweeping line
# First mark points where there are changes,
# i.e. (i - 1) with +k and j with -k, then do running sum
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        
        curr = 0
        
        for i in range(n):
            curr += res[i]
            res[i] = curr
        
        res.pop()
        
        return res

# Solution 2, segment tree
# t.b.c
