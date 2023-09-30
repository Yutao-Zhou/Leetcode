class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        #### DP ####
        memo = [[0 for i in range(len(dungeon[0]))] for i in range(len(dungeon))]
        # Base case #
        memo[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for y in range(len(dungeon) - 2, -1, -1):
            memo[y][-1] = max(1, memo[y + 1][-1] - dungeon[y][-1])
        for x in range(len(dungeon[0]) - 2, -1, -1):
            memo[-1][x] = max(1, memo[-1][x + 1] - dungeon[-1][x])
        # Fill memo table, min becuase we want lower start hp, max becuase we need on 1 hp if the start hp needed is lower than 1 #
        for y in range(len(dungeon) - 2, -1, -1):
            for x in range(len(dungeon[0]) - 2, -1, -1):
                memo[y][x] = max(1, min(memo[y + 1][x] -  dungeon[y][x], memo[y][x + 1] -  dungeon[y][x]))
        return memo[0][0]