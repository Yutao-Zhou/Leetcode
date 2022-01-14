class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #### map and compare number ####
        # tmap = {}
        # amap = {}
        # for i in target:
        #     if i in tmap:
        #         tmap[i] += 1
        #     if i not in tmap:
        #         tmap[i] = 1
        # for i in arr:
        #     if i in amap:
        #         amap[i] += 1
        #     if i not in amap:
        #         amap[i] = 1
        # return tmap == amap
        
        #### sort and compare ####
        # return sorted(target) == sorted(arr)
        
        #### use list as hashmap ####
        check = [0] * 1001
        for i in target:
            check[i] += 1
        for j in arr:
            check[j] -= 1
        return check == [0] * 1001