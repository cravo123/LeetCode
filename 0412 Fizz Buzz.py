# Solution 1, simulation
class Solution:
    def change(self, i):
        if i % 15 == 0:
            res = 'FizzBuzz'
        elif i % 5 == 0:
            res = 'Buzz'
        elif i % 3 == 0:
            res = 'Fizz'
        else:
            res = str(i)
        return res
    
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        res = [self.change(i) for i in range(1, n + 1)]
        
        return res

# Solution 1.1, more general solution when it is FizzBuzzJazz
class Solution:
    def change(self, idx):
        res = str(idx)
        if idx % 3 == 0 or idx % 5 == 0:
            res = 'Fizz' * (idx % 3 == 0) + 'Buzz' * (idx % 5 == 0)
        
        return res
            
    def fizzBuzz(self, n: int) -> List[str]:
        res = [self.change(i) for i in range(1, n + 1)]
        
        return res