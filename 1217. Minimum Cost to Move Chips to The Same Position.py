class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ##########################################
        ### real human hard solving thinking #####
        ##########################################
        # ans = 0
        # count = {}
        # even = 0
        # odd = 0
        # target = -1
        # for i in position:
        #     if i in count:
        #         count[i] += 1
        #     if i not in count:
        #         count[i] = 1
        #     if i % 2 == 0:
        #         even += 1
        #     if i % 2 == 1:
        #         odd += 1
        # va = max(count.values())
        # ls = [k for k, v in count.items() if v == va]
        # if even > odd:
        #     for i in ls:
        #         if i % 2 == 0:
        #             target = i
        #     if target == -1:
        #         target = ls[0] + 1
        # else:
        #     for i in ls:
        #         if i % 2 == 1:
        #             target = i
        #     if target == -1:
        #         target = ls[0] + 1
        # for i in position:
        #     ans += (i - target) % 2
        # return ans
    
        ###########################
        ### even odd solution #####
        ###########################
        even = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            if i % 2 == 1:
                odd += 1
        if even >= odd:
            return len(position) - even
        else:
            return len(position) - odd