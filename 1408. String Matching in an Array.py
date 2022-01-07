class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #### fake solution, check ####
        # ans = []
        # for i in range(len(words)):
        #     for j in range(i + 1,len(words)):
        #         if words[j] in words[i]:
        #             ans.append(words[j])
        #         if words[i] in words[j]:
        #             ans.append(words[i])
        # return list(set(ans))
        
        #### join and count occurence ####
        ans = []
        allWords = " ".join(words)
        for word in words:
                if allWords.count(word) > 1:
                    ans.append(word)
        return ans