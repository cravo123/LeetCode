# Solution 1, Recursion
class Solution:
    def dfs(self, price, needs, special):
        if any(q < 0 for q in needs):
            return float('inf')
        
        if all(q == 0 for q in needs):
            return 0
        
        # total price without using any speical offers
        res = sum(p * q for p, q in zip(price, needs))
        
        for offer in special:
            if all(q2 <= q1 for q1, q2 in zip(needs, offer)):
                new_needs = [q1 - q2 for q1, q2 in zip(needs, offer)]
                res = min(res, offer[-1] + self.dfs(price, new_needs, special))
        
        return res
    
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        res = self.dfs(price, needs, special)
        
        return res

# Solution 2, Memoization
class Solution:
    def dfs(self, price, needs, special, d):
        if needs in d:
            return d[needs]
        
        if any(q < 0 for q in needs):
            return float('inf')
        
        if all(q == 0 for q in needs):
            return 0
        
        res = sum(p * q for p, q in zip(price, needs))
        
        for offer in special:
            if all(q2 <= q1 for q1, q2 in zip(needs, offer)):
                new_needs = tuple([q1 - q2 for q1, q2 in zip(needs, offer)])
                res = min(res, offer[-1] + self.dfs(price, new_needs, special, d))
        
        d[needs] = res
        return res
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        d = {}
        needs = tuple(needs)
        res = self.dfs(price, needs, special, d)
        
        return res