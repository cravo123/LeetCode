import collections

# Solution 1, hashmap
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.idx = 0
        self.size = n
        
        self.discount = 1 - discount / 100
        
        self.prices = collections.defaultdict(int)
        
        for id_, p in zip(products, prices):
            self.prices[id_] = p
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.idx = (self.idx + 1) % self.size
        
        cost = sum(self.prices[id_] * cnt for id_, cnt in zip(product, amount))
        
        cost = cost * self.discount if self.idx == 0 else cost
        
        return cost
        

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)