# Solution 1, simulation

class Solution:
    def change(self, name):
        idx = name.find('+')
        if idx >= 0:
            name = name[:idx]
        name = name.replace('.', '')
        return name
        
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        res = set()
        
        for email in emails:
            local_name, domain_name = email.strip().split('@')
            
            res.add((self.change(local_name), domain_name))
        
        return len(res)
