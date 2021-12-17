class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        #### map all word ####
        # word1 = ""
        # word2 = ""
        # target = ""
        # mapdic = {"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6","h":"7","i":"8","j":"9"}
        # for i in firstWord:
        #     word1 += mapdic[i]
        # word1 = int(word1)
        # for i in secondWord :
        #     word2 += mapdic[i]
        # word2 = int(word2)
        # for i in targetWord :
        #     target += mapdic[i]
        # target = int(target)
        # return word1 + word2 == target
        
        #### ascii list inplace ####
        # map firstWord
        firstWord = list(firstWord)
        for i in range(-1,-len(firstWord) - 1,-1):
            firstWord[i] = chr(ord(firstWord[i]) - 49)
        firstWord = int("".join(firstWord))
        # map secondWord
        secondWord = list(secondWord)
        for i in range(-1,-len(secondWord) - 1,-1):
            secondWord[i] = chr(ord(secondWord[i]) - 49)
        secondWord = int("".join(secondWord))
        # map targetWord
        targetWord = list(targetWord)
        for i in range(-1,-len(targetWord) - 1,-1):
            targetWord[i] = chr(ord(targetWord[i]) - 49)
        targetWord = int("".join(targetWord))
        # return answer check
        return firstWord + secondWord == targetWord