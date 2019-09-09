# Solution 1
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A.reverse()
        carry = K
        
        for i, v in enumerate(A):
            v += carry
            carry, v = divmod(v, 10)
            A[i] = v
        
        while carry:
            A.append(carry % 10)
            carry //= 10
        
        A.reverse()
        
        return A

# Solution 1.1, without reversing
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = K
        idx = len(A) - 1
        
        while idx >= 0 and carry:
            carry, val = divmod(carry + A[idx], 10)
            A[idx] = val
            idx -= 1
        
        while carry:
            carry, val = divmod(carry, 10)
            A = [val] + A
        return A