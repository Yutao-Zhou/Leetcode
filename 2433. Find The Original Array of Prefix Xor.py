class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #### ordinary XOR ####
        # ans = [pref[0]]
        # for i in range(1, len(pref)):
        #     ans.append(pref[i - 1] ^ pref[i])
        # return ans

        #### reverse recreate space optimised ####
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref