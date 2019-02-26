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