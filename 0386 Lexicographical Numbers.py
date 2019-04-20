class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        q = [i for i in range(1, n + 1)]
        
        q.sort(key=lambda x: str(x))
        
        return q