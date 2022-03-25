class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        #### brue force ####
        n = len(searchWord)
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if sentence[i][:n] == searchWord:
                return(i + 1)
        return -1