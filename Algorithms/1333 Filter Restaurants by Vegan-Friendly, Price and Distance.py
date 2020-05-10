# Solution 1, simulation
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        res = [[r, i] for i, r, v, p, d in restaurants
              if p <= maxPrice and d <= maxDistance and (v if veganFriendly else True)]
        
        res.sort(reverse=True)
        
        res = [i for _, i in res]
        
        return res