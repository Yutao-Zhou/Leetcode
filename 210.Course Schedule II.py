class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #### BFS #####
        indegree = [0] * (numCourses)
        queue = []
        order = []
        prerequest = {}
        for pre in prerequisites:
            indegree[pre[0]] += 1
            if pre[1] not in prerequest:
                prerequest[pre[1]] = [pre[0]]
            else:
                prerequest[pre[1]].append(pre[0])
        while 0 in indegree:
            index = indegree.index(0)
            order.append(indegree.index(0))
            if index not in prerequest:
                indegree[index] = -1
                pass
            else:
                for course in prerequest[index]:
                    indegree[course] -= 1
                indegree[index] = -1
        if len(order) == numCourses:
            return order
        return []