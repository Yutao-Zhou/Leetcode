class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #### Sorting ####
        # ans = [""] * len(score)
        # score_map = list(zip(score, range(len(score))))
        # score_map.sort(key=lambda x:-x[0])
        # for i in range(len(score_map)):
        #     if i == 0:
        #         ans[score_map[i][1]] = "Gold Medal"
        #     elif i == 1:
        #         ans[score_map[i][1]] = "Silver Medal"
        #     elif i == 2:
        #         ans[score_map[i][1]] = "Bronze Medal"
        #     else:
        #         ans[score_map[i][1]] = str(i + 1)
        # return ans

        #### max heap ####
        import heapq
        ans = [""] * len(score)
        score_map = []
        for i in range(len(score)):
            heapq.heappush(score_map, (-score[i], i))
        rank = 1
        while score_map:
            _, i = heapq.heappop(score_map)
            if rank == 1:
                ans[i] = "Gold Medal"
            elif rank == 2:
                ans[i] = "Silver Medal"
            elif rank == 3:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(rank)
            rank += 1
        return ans