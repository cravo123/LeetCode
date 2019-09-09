# Solution 1, Simulating stack operations
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q = []
        
        i = j = 0
        
        n = len(pushed)
        
        while i < n and j < n:
            while q and q[-1] == popped[j]:
                q.pop()
                j += 1
            q.append(pushed[i])
            i += 1
        
        while j < n and q[-1] == popped[j]:
            q.pop()
            j += 1
        
        return i == j == n and not q

# Solution 2
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q = []
        j = 0
        n = len(popped)
        
        for c in pushed:
            q.append(c)
            
            while q and q[-1] == popped[j]:
                j += 1
                q.pop()
        return j == n