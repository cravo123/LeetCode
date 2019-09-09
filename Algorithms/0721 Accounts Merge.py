import collections

# Solution 1, DFS, need to cache two mappings
# email -> set([ids])
# id -> set(emails)
class Solution:
    def dfs(self, idx, res, seen, emails, ids):
        seen.add(idx)
        res |= set(ids[idx])
        
        for new_email in ids[idx]:
            for j in emails[new_email]:
                if j not in seen:
                    self.dfs(j, res, seen, emails, ids)
        
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = collections.defaultdict(set)   # email: set([ids])
        ids = collections.defaultdict(set)      # id: set([emails])
        
        for i, account in enumerate(accounts):
            ids[i] |= set(account[1:])
            
            for x in account[1:]:
                emails[x].add(i)
        
        res = []
        seen = set()
        
        for i in range(len(accounts)):
            if i not in seen:
                t_res = set()
                self.dfs(i, t_res, seen, emails, ids)
                res.append([accounts[i][0]] + list(sorted(t_res)))
        
        return res