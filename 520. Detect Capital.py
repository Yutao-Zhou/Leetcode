class Solution:
    def detectCapitalUse(self, word: str) -> bool:
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
        # if 65 <= ord(word[0]) <= 90:
        #     counter = 0
        #     for i in word:
        #         if 65 <= ord(i) <= 90:
        #             counter += 1
        #     if counter == len(word) or counter == 1:
        #         return True
        #     else:
        #         return False
        # if 97 <= ord(word[0]) <= 122:
        #     for i in word:
        #         if 65 <= ord(i) <= 90:
        #             return False
        #     return True
        
        #### another way ####
        if len(word) == 1:
            return True
        elif "a" <= word[0] <= "z":
            for i in word:
                    if i < "a" or i > "z":
                        return False
        elif "A" <= word[0] <= "Z":
            if "A" <= word[1] <= "Z":
                for i in word:
                    if i < "A" or i > "Z":
                        return False
            if "a" <= word[1] <= "z":
                for i in range(1,len(word)):
                    if word[i] < "a" or word[i] > "z":
                        return False
        return True