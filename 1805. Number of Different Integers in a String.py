class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        #### pre processed and set####
        # word += " "
        # numbers = []
        # cache = ""
        # for i in word:
        #     if 48 <= ord(i) <= 57:
        #         cache += i
        #     elif (ord(i) > 57 or ord(i) < 48) and cache != "":
        #         numbers.append(int(cache))
        #         cache = ""
        # return len(set(numbers))
        
        #### two pointer count ####
        # word += " "
        # numbers = []
        # i = 0
        # j = 1
        # ans = 0
        # while j < len(word):
        #     if ord(word[i]) > 57 or ord(word[i]) < 48:
        #         i += 1
        #         j = i + 1
        #     elif 48 <= ord(word[i]) <= 57:
        #         if 48 <= ord(word[j]) <= 57:
        #             j += 1
        #             if j == len(word):
        #                 if int(word[i:j]) not in numbers:
        #                     return len(numbers) + 1
        #                 if int(word[i:j]) in numbers:
        #                     return len(numbers)
        #         elif (ord(word[j]) > 57 or ord(word[j]) < 48):
        #             if int(word[i:j]) not in numbers:
        #                 numbers.append(int(word[i:j]))
        #                 i = j + 1
        #                 j = i + 1
        #             elif int(word[i:j]) in numbers:
        #                 i = j + 1
        #                 j = i + 1
        # return len(numbers)
        
        #### is index ####
        # word += " "
        # numbers = set()
        # cache = ""
        # for c in word:
        #     if c.isdigit():
        #         cache += c
        #     elif cache != "":
        #         numbers.add(int(cache))
        #         cache = ""
        # return len(numbers)
        
        #### find all ####
        return len(set(map(int, re.findall(r'\d+', word))))