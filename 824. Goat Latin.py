class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if sentence[i][0] not in vowel:
                sentence[i] = sentence[i][1:] + sentence[i][0]
            sentence[i] += "ma" + "a" * (i + 1)
        return " ".join(sentence)