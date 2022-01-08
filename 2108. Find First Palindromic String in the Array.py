class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #### reverse, not real solution ####
        # for i in words:
        #     if i == i[::-1]:
        #         return i
        # return ""
        
        #### two pointer ####
        for word in words:
            i = 0
            j = len(word) - 1
            while word[i] == word[j]:
                i += 1
                j -= 1
                if i >= j:
                    return word
        return ""