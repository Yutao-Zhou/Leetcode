class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #### hash map and recreat ####
        # def frequencyTable(arr):
        #     table = {}
        #     for n in arr:
        #         if n in table:
        #             table[n] += 1
        #         if n not in table:
        #             table[n] = 1
        #     return table
        # arr1Map = frequencyTable(arr1)
        # arr2Map = frequencyTable(arr2)
        # ans = []
        # cache = []
        # for key in arr2Map.keys():
        #     ans += [key] * arr1Map[key]
        # for key in arr1Map.keys():
        #     if key not in ans:
        #         cache.append(key)
        # cache = sorted(cache)
        # for n in cache:
        #     ans += [n] * arr1Map[n]
        # return ans
        
        #### sort and pop ####
        ans = []
        arr1 = sorted(arr1)
        for target in arr2:
            i = 0
            while i < len(arr1):
                if arr1[i] == target:
                    ans.append(arr1.pop(i))
                else:
                    i += 1
        ans += arr1
        return ans