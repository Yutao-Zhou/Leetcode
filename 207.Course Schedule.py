class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #### BFS #####
        indegree = [0] * (numCourses)
        queue = []
        prerequest = {}
        for pre in prerequisites:
            indegree[pre[0]] += 1
            if pre[1] not in prerequest:
                prerequest[pre[1]] = [pre[0]]
            else:
                prerequest[pre[1]].append(pre[0])
        while 0 in indegree:
            index = indegree.index(0)
            if index not in prerequest:
                indegree[index] = -1
                pass
            else:
                for course in prerequest[index]:
                    indegree[course] -= 1
                indegree[index] = -1
        for i in indegree:
            if i > 0:
                return False
        return True