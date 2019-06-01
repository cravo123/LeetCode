# Solution 1, partition in quick sort
class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        j = -1
        
        for i, v in enumerate(A):
            if v % 2 == 0:
                j += 1
                A[i], A[j] = A[j], A[i]
        
        return A

# Solution 1.1, quick-select, two-pointer
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            
            while i < j and A[j] % 2 == 1:
                j -= 1
            
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        
        return A

# Solution 2, customized sorting
class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        A.sort(key=lambda x: x % 2)
        return A