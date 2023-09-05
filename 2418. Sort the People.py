class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #### Map and srot ####
        ans = []
        height_map = {}
        for i in range(len(names)):
            height_map[heights[i]] = names[i]
        heights.sort(reverse=True)
        for h in heights:
            ans.append(height_map[h])
        return ans