class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = {}
        luck = []
        for i in arr:
            if i in frequency:
                frequency[i] += 1
            if i not in frequency:
                frequency[i] = 1
        for i in frequency.items():
            if i[0] == i[1]:
                luck.append(i[0])
        if luck == []:
            return -1
        else:
            return max(luck)