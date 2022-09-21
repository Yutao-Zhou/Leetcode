class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #### Record Path ####
        # ans = set()
        # def backtrack(remain, current):
        #     ans.add(current)
        #     l = len(remain)
        #     if l > 0:
        #         for i in range(l):
        #             backtrack(remain[:i] + remain[i + 1:], current + remain[i])
        # backtrack(tiles, "")
        # return len(ans) - 1
        
        #### frequency map ####
        # freqMap = [0] * 26
        # for c in tiles:
        #     freqMap[ord(c) - 65] += 1
        # def backtrack(remain):
        #     ans = 0
        #     for i in range(26):
        #         if not remain[i]:
        #             continue
        #         remain[i] -= 1
        #         ans += backtrack(remain) + 1
        #         remain[i] += 1
        #     return ans
        # return backtrack(freqMap)
        
        #### String Manipulation ####
        # def backtrack(remain):
        #     ans = 0
        #     used = set()
        #     for i in range(len(remain)):
        #         if remain[i] not in used:
        #             used.add(remain[i])
        #             ans += backtrack(remain[:i] + remain[i + 1:]) + 1
        #     return ans
        # return backtrack(tiles)
        
        #### Sort ####
        def backtrack(remain):
            ans = 0
            for i in range(len(remain)):
                if i == 0 or remain[i] != remain[i - 1]:
                    ans += backtrack(remain[:i] + remain[i + 1:]) + 1
            return ans
        remain = list(tiles)
        remain.sort()
        return backtrack(remain)