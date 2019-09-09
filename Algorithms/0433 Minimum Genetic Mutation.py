# Solution 1, double-ended BFS
class Solution:
    def change(self, word, bank, seen):
        for i in range(len(word)):
            for c in 'ACGT':
                new_word = word[:i] + c + word[(i + 1):]
                if new_word not in seen and new_word in bank:
                    yield new_word
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        
        left = set([start])
        right = set([end])
        seen = set()
        
        steps = 0
        
        while left and right:
            tmp = set()
            
            for word in left:
                if word in right:
                    return steps
                seen.add(word)
                for new_word in self.change(word, bank, seen):
                    tmp.add(new_word)
            
            steps += 1
            left, right = right, tmp
        
        return -1

# Solution 2, reuse Bank
class Solution:
    def change(self, word, bank):
        for i in range(len(word)):
            for c in 'ACGT':
                new_word = word[:i] + c + word[(i + 1):]
                if new_word in bank:
                    yield new_word
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        
        left = set([start])
        right = set([end])
        
        steps = 0
        
        while left and right:
            tmp = set()
            
            for word in left:
                if word in right:
                    return steps
                bank.discard(word)
                for new_word in self.change(word, bank):
                    tmp.add(new_word)
            
            steps += 1
            left, right = right, tmp
        
        return -1