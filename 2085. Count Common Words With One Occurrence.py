class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        #### frequency ####
        # check1 = {}
        # check2 = {}
        # ans = 0
        # for i in words1:
        #     if i in check1:
        #         check1[i] += 1
        #     if i not in check1:
        #         check1[i] = 1
        # for i in words2:
        #     if i in check2:
        #         check2[i] += 1
        #     if i not in check2:
        #         check2[i] = 1
        # if len(words1) >= len(words2):
        #     for i in check2.items():
        #         if i[1] == 1 and i[0] in check1 and check1[i[0]] == 1:
        #             ans += 1
        # if len(words1) < len(words2):
        #     for i in check1.items():
        #         if i[1] == 1 and i[0] in check2 and check2[i[0]] == 1:
        #             ans += 1
        # return ans
        
        #### count fake solution ####
        # ans = 0
        # for i in words1:
        #     if words1.count(i) == 1 and words2.count(i) == 1:
        #         ans += 1
        # return ans
        
        #### list check ####
        check = []
        remove = []
        ans = 0
        words2.sort()
        i = 0
        words2.insert(0,"Begin")
        words2.append("End")
        for string in words1:
            if string in check:
                remove.append(string)
            elif string not in check:
                check.append(string)
        while words2[i] != "End":
            if words2[i] != words2[i - 1] and words2[i] != words2[i + 1] and words2[i] in check and words2[i] not in remove:
                ans += 1
            i += 1
        return ans