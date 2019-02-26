import collections
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        q = collections.deque([i for i in range(n)])
        
        res = [0 for _ in deck]
        idx = 0
        while q:
            i = q.popleft()
            res[i] = deck[idx]
            idx += 1
            if q:
                q.append(q.popleft())
        return res