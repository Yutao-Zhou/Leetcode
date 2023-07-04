class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        #Greedy
        ans = len(tops)
        valid = [0] * 6
        costTop = [0] * 6
        costBottom = [0] * 6
        for i, number in enumerate(tops):
            valid[number - 1] += 1
            if number != bottoms[i]:
                costTop[number - 1] += 1
                costBottom[bottoms[i] - 1] += 1
                valid[bottoms[i] - 1] += 1
        for i, v in enumerate(valid):
            if v == len(tops):
                ans = min(ans, costTop[i], costBottom[i])
        if ans != len(tops):
            return ans
        return -1