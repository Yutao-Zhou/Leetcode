class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #### upper and lower trick ####
        # if 65 <= ord(word[0]) <= 90:
        #     word = word[1:]
        #     if word.upper() == word or word.lower() == word:
        #         return True
        #     else:
        #         return False
        # if 97 <= ord(word[0]) <= 122:
        #         if word.lower() != word:
        #             return False
        # return True
        
        #### one pass ####
        if 65 <= ord(word[0]) <= 90:
            counter = 0
            for i in word:
                if 65 <= ord(i) <= 90:
                    counter += 1
            if counter == len(word) or counter == 1:
                return True
            else:
                return False
        if 97 <= ord(word[0]) <= 122:
            for i in word:
                if 65 <= ord(i) <= 90:
                    return False
            return True