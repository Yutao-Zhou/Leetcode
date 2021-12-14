class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split(" ")
        counter = 0
        cach1 = 0
        cach2 = 0
        sentence = [i for i in sentence if i.strip()!='']
        for i in sentence:
            cach1 = 0
            cach2 = 0
            for j in range(len(i)):
                if ord(i[j]) >= 48 and ord(i[j]) <= 57:
                    counter += 1
                    break
                if i[j] == "-":
                    cach1 += 1
                    if j == 0 or j == len(i) - 1:
                        counter += 1
                        break
                    elif ord(i[j - 1]) < 97 or ord(i[j - 1]) > 122 or ord(i[j + 1]) < 97 or ord(i[j + 1]) > 122:
                        counter += 1
                        break
                    elif cach1 > 1:
                        counter += 1
                        break
                if i[j] == "!" or i[j] == "." or i[j] == ",":
                    cach2 += 1
                    if j != len(i) - 1:
                        counter += 1
                        break
                    elif cach2 > 1:
                        counter += 1
                        break
        return len(sentence) - counter