# Solution 1, partition in quick sort
class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        j = -1
        
        for i, v in enumerate(A):
            if v % 2 == 0:
                j += 1
                A[i], A[j] = A[j], A[i]
        
        return A

# Solution 2, customized sorting
class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        A.sort(key=lambda x: x % 2)
        return A