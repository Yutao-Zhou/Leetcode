class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        #### Brute Force with Hashmap ####
        # ans, UAM = [0] * k, {}
        # for userID, activeTime in logs:
        #     if userID not in UAM:
        #         UAM[userID] = set()
        #     if userID in UAM:
        #         UAM[userID].add(activeTime)
        # for time in UAM.values():
        #     ans[len(time) - 1] += 1
        # return ans
        
        #### Doulble Sort ####
        ans, counter = [0] * k, 1
        logs.sort()
        for i in range(1,len(logs)):
            if logs[i][0] != logs[i - 1][0]:
                ans[counter - 1] += 1
                counter = 1
            elif logs[i][1] != logs[i - 1][1]:
                    counter += 1
        ans[counter - 1] += 1
        return ans