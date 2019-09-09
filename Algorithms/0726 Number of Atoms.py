import collections

# Solution 1, Iteration
class Solution:
    def tokenize(self, formula):
        q = []
        i, n = 0, len(formula)
        
        while i < n:
            c = formula[i]
            if c.isupper():
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                q.append(formula[i:j])
                i = j
            elif c.isdigit():
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                q.append(formula[i:j])
                i = j
            else:
                q.append(c)
                i += 1
        return q
        
    def countOfAtoms(self, formula: str) -> str:
        xs = self.tokenize(formula)
        
        q = []
        i, n = 0, len(xs)
        d = collections.Counter()
        while i < n:
            c = xs[i]
            if c.isalpha():
                if i < n - 1 and xs[i + 1].isdigit():
                    cnt = int(xs[i + 1])
                    i += 2
                else:
                    cnt = 1
                    i += 1
                d[c] += cnt
            elif c == '(':
                q.append(d)
                q.append('(')
                d = collections.Counter()
                i += 1
            else:
                while q and q[-1] != '(':
                    d += q.pop()
                q.pop()
                
                if i < n - 1 and xs[i + 1].isdigit():
                    cnt = int(xs[i + 1])
                    i += 2
                else:
                    cnt = 1
                    i += 1
                for c in d:
                    d[c] *= cnt
            
        while q:
            d += q.pop()
        
        res = [v + (str(d[v]) if d[v] > 1 else '') for v in sorted(d)]
        res = ''.join(res)
        return res
        

# Solution 2, Recursion
# Find the cut for each pair of parenthesis and recursion on each substring
class Solution:
    def tokenize(self, formula):
        q = []
        i, n = 0, len(formula)
        
        while i < n:
            c = formula[i]
            if c.isupper():
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                q.append(formula[i:j])
                i = j
            elif c.isdigit():
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                q.append(formula[i:j])
                i = j
            else:
                q.append(c)
                i += 1
        return q
    
    def parse(self, xs, left, right):
        d = collections.Counter()
        
        if left == right:
            d[xs[left]] += 1
        
        if left >= right:
            return d
        
        if xs[left].isalpha():
            if xs[left + 1].isdigit():
                d[xs[left]] += int(xs[left + 1])
                d += self.parse(xs, left + 2, right)
            else:
                d[xs[left]] += 1
                d += self.parse(xs, left + 1, right)
        else:
            i = left
            cnt = 0
            while i <= right:
                if xs[i] == '(':
                    cnt += 1
                elif xs[i] == ')':
                    cnt -= 1
                if cnt == 0:
                    break
                i += 1
                
            v = self.parse(xs, left + 1, i - 1)
            if i == right or not xs[i + 1].isdigit():
                cnt = 1
                i += 1
            else:
                cnt = int(xs[i + 1])
                i += 2
            for c in v:
                d[c] += v[c] * cnt
            d += self.parse(xs, i, right)
        return d      
    
    def countOfAtoms(self, formula: str) -> str:
        xs = self.tokenize(formula)
        
        d = self.parse(xs, 0, len(xs) - 1)
        
        res = [v + (str(d[v]) if d[v] > 1 else '') for v in sorted(d)]
        
        res = ''.join(res)
        
        return res