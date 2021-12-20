class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #### hard solve ####
        # frequency = {}
        # ans = []
        # i = 0
        # for letter in words[0]:
        #     ans.append(letter)
        # ans.sort()
        # while i < len(words):
        #     i += 1
        #     j = 0
        #     if i == len(words) and j == 0:
        #         return ans
        #     while j < len(ans):
        #         if ans[j] not in words[i]:
        #             ans.remove(ans[j])
        #         elif ans[j] in words[i]:
        #             if ans.count(ans[j]) > words[i].count(ans[j]):
        #                 ans.remove(ans[j])
        #             else:
        #                 j += 1
        
        #### a little bit smarter version ####
        words = sorted(words, key=len)
        frequency = {}
        ans = []
        i = 0
        for letter in words[0]:
            ans.append(letter)
        while i < len(words):
            i += 1
            j = 0
            if i == len(words) and j == 0:
                return ans
            while j < len(ans):
                if ans[j] not in words[i]:
                    ans.remove(ans[j])
                elif ans[j] in words[i]:
                    if ans.count(ans[j]) > words[i].count(ans[j]):
                        ans.remove(ans[j])
                    else:
                        j += 1