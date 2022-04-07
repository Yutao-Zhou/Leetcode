class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #### regular BFS ####
        # maxtime = 0
        # que = deque([(headID, 0)])
        # while que:
        #     current = que.popleft()
        #     leader = current[0]
        #     time = current[1]
        #     if informTime[leader] != 0:
        #         inform = informTime[leader]
        #         for i in range(len(manager)):
        #             if manager[i] == leader:
        #                 que.append((i, time + inform))
        #     if informTime[leader] == 0 and time > maxtime:
        #         maxtime = time
        # return maxtime
        
        #### speed up BFS ####
        maxtime = 0
        que = deque([(headID, 0)])
        network = {}
        for i in range(len(manager)):
            if manager[i] in network:
                network[manager[i]].append(i)
            if manager[i] not in network:
                network[manager[i]] = [i]
        while que:
            current = que.popleft()
            leader = current[0]
            time = current[1]
            if informTime[leader] != 0:
                inform = informTime[leader]
                for p in network[leader]:
                    que.append((p, time + inform))
            if informTime[leader] == 0 and time > maxtime:
                maxtime = time
        return maxtime