class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #### find max number possible ####
        # ans = 0
        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 1 and n > 0:
        #         return False
        #     if flowerbed[0] == 0 and n < 2:
        #         return True
        # else:
        #     if flowerbed[1] == 0 == flowerbed[0]:
        #         flowerbed[0] = 1
        #         ans += 1
        #     for i in range(1,len(flowerbed) - 1):
        #         if flowerbed[i - 1] == 0 == flowerbed[i + 1] == flowerbed[i]:
        #             flowerbed[i] = 1
        #             ans += 1
        #     if flowerbed[-2] == 0 == flowerbed[-1] == flowerbed[i]:
        #         flowerbed[-1] = 1
        #         ans += 1
        # return ans >= n
        
        #### break when reach ####
        # ans = 0
        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 1 and n > 0:
        #         return False
        #     if flowerbed[0] == 0 and n < 2:
        #         return True
        # else:
        #     if flowerbed[1] == 0 == flowerbed[0]:
        #         flowerbed[0] = 1
        #         ans += 1
        #     for i in range(1,len(flowerbed) - 1):
        #         if flowerbed[i - 1] == 0 == flowerbed[i + 1] == flowerbed[i]:
        #             flowerbed[i] = 1
        #             ans += 1
        #         if ans == n:
        #             return True
        #     if flowerbed[-2] == 0 == flowerbed[-1] == flowerbed[i]:
        #         flowerbed[-1] = 1
        #         ans += 1
        # return ans >= n
        
        #### count zeros ####
        ans = 0
        counter = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in flowerbed:
            if i == 0:
                counter += 1
            if i == 1:
                ans += (counter - 1) // 2
                counter = 0
        ans += (counter - 1) // 2
        return ans >= n