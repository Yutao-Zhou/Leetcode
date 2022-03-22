class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #### no thinking only map ####
        # ans = words1
        # words2 = list(set(words2))
        # one = {}
        # two = {}
        # for word in words1:
        #     one[word] = {}
        #     for char in word:
        #         if char not in one[word]:
        #             one[word][char] = 1
        #         else:
        #             one[word][char] += 1
        # for word in words2:
        #     two[word] = {}
        #     for char in word:
        #         if char not in two[word]:
        #             two[word][char] = 1
        #         else:
        #             two[word][char] += 1
        # for word1 in one.keys():
        #     stop = False
        #     for check in two.keys():
        #         for char in two[check]:
        #             if char in one[word1]:
        #                 if two[check][char] <= one[word1][char]:
        #                     pass
        #                 else:
        #                     try:
        #                         ans.remove(word1)
        #                     except:
        #                         pass
        #                     stop = True
        #                     break
        #             else:
        #                 try:
        #                     ans.remove(word1)
        #                 except:
        #                     pass
        #                 stop = True
        #                 break
        #         if stop == True:
        #             break
        # return ans
        
        #### smarter mapping by joining words2 ####
        ans = []
        two = [0] * 26
        for word in words2:
            for char in word:
                if word.count(char) > two[ord(char) - 97]:
                    two[ord(char) - 97] = word.count(char)
                if word.count(char) > 10:
                    return []
        for word in words1:
            for i in range(26):
                if two[i] > word.count(chr(i + 97)):
                    break
                if i == 25 and two[i] <= word.count(chr(i + 97)):
                    ans.append(word)
        return ans