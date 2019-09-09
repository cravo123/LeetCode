# Solution 1, simulation
# first cache all not-equal indices
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(A)
        
        q = []
        
        for a, b in zip(A, B):
            if a != b:
                q.append([a, b])
        
        return len(q) == 2 and q[0] == q[1][::-1]

# Solution 2, Two-Pointer
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        i = 0
        j = len(A) - 1
        
        while i < j and A[i] == B[i]:
            i += 1
        
        while i < j and A[j] == B[j]:
            j -= 1
        
        if i < j:
            if A[i] != B[j] or A[j] != B[i]:
                return False
            
            i += 1
            j -= 1
            while i < j and A[i] == B[i]:
                i += 1
            return i >= j
        else:
            if len(A) > len(set(A)):
                return True
        return False