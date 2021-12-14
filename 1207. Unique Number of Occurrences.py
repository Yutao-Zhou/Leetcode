class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ##### count frequency by myself #####
        # frequency = {}
        # cache = []
        # for num in arr:
        #     if num in frequency:
        #         frequency[num] += 1
        #     if num not in frequency:
        #         frequency[num] = 1
        # for freq in frequency.values():
        #     cache.append(freq)
        # return len(cache) == len(set(cache))
        
        ##### use counter and set #####
        frequency = Counter(arr)
        return len(frequency.values()) == len(set(frequency.values()))