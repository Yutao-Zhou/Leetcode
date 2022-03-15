class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #### connection map ####
        # ans = []
        # preDic = {}
        # for pair in prerequisites:
        #     if pair[1] not in preDic:
        #         preDic[pair[1]] = [pair[0]]
        #     else:
        #         preDic[pair[1]].append(pair[0])
        # for i in preDic:
        #     for num in preDic[i]:
        #         if num in preDic.keys():
        #             preDic[i].extend(preDic[num])
        # for i in queries:
        #     if i[1] not in preDic.keys():
        #         ans.append(False)
        #     else:
        #         if i[0] in preDic[i[1]]:
        #             ans.append(True)
        #         else:
        #             ans.append(False)
        # return ans
        
        #### Floyd–Warshall Algorithm ####
        connected = [[False] * numCourses for i in range(numCourses)]

        for i, j in prerequisites:
            connected[i][j] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
        return [connected[i][j] for i, j in queries]