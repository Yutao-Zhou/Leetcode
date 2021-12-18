class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #### force check ####
        # ans = 0
        # text = text.split(" ")
        # if brokenLetters == "":
        #     return len(text)
        # brokenLetters = list(brokenLetters)
        # for word in text:
        #     for i in range(len(brokenLetters)):
        #         if brokenLetters[i] in word:
        #             break
        #         if i == len(brokenLetters) - 1: 
        #             ans += 1
        # return ans
        
        #### set ####
        brokenLetters = set(brokenLetters)
        text = text.split(" ")
        ans = 0
        for words in text:
            if brokenLetters.intersection(set(words)) == set():
                ans += 1
        return ans