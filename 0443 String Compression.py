# Solution 1, simulation
# Similar to running length encoding
# But we got repeated codes after for loop
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        curr = chars[0]
        cnt = 0
        j = 0
        
        for c in chars:
            if curr == c:
                cnt += 1
            else:
                chars[j] = curr
                j += 1
                if cnt > 1:
                    width = len(str(cnt))
                    chars[j:(j + width)] = str(cnt)
                    j += width
                curr = c
                cnt = 1
        
        chars[j] = curr
        j += 1
        if cnt > 1:
            width = len(str(cnt))
            chars[j:(j + width)] = str(cnt)
            j += width
        
        return j

# Solution 2, manual control for loop using while loop
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, n = 0, len(chars)
        idx = 0
        
        while i < n:
            curr = chars[i]
            cnt = 0
            
            while i < n and chars[i] == curr:
                cnt += 1
                i += 1
            
            chars[idx] = curr
            idx += 1
            
            if cnt > 1:
                cnt = list(str(cnt))
                chars[idx:(idx + len(cnt))] = cnt
                idx += len(cnt)
        
        return idx