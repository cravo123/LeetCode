"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def dfs(self, idx, d):
        res = d[idx][0]
        
        for i in d[idx][1]:
            res += self.dfs(i, d)
        
        return res
        
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        
        for employee in employees:
            d[employee.id] = [employee.importance, employee.subordinates]
        
        res = self.dfs(id, d)
        
        return res