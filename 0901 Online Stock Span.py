class StockSpanner(object):

    def __init__(self):
        self.q = [[-1, float('inf')]]       
        self.cnt = 0
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.q and self.q[-1][1] <= price:
            self.q.pop()
            
        res = max(res, self.cnt - self.q[-1][0])
        self.q.append([self.cnt, price])
        self.cnt += 1
        
        return res
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)