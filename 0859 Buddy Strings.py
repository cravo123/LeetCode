# Solution 1,
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        cans = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                cans.append(i)
        
        if len(cans) == 0:
            return len(A) > len(set(A))
        else:
            return len(cans) == 2 and A[cans[0]] == B[cans[1]] and A[cans[1]] == B[cans[0]]

# Solution 2, Two Pointers
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