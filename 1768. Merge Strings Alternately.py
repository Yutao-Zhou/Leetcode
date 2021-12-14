class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #### list #####
        # ans = []
        # i = 0
        # j = 0
        # while 1:
        #     if i >= len(word1) and j >= len(word2):
        #         break
        #     if i < len(word1):
        #         ans.append(word1[i])
        #         i += 1
        #     if j < len(word2):
        #         ans.append(word2[j])
        #         j += 1
        # return "".join(ans)
        
        ##### keep it string #####
        ans = ""
        for i in range(min(len(word1),len(word2))):
            ans += word1[i] + word2[i]
        ans += word1[i+1:] + word2[i+1:]
        return ans