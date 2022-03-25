"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #### DFS time: O(N) space: O(N) ####
        emap = {}
        for e in employees:
            emap[e.id] = e
        def dfs(eid):
            employee = emap[eid]
            subordinates_importance = sum(dfs(eid) for eid in employee.subordinates)
            return subordinates_importance + employee.importance
        return dfs(id)