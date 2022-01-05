class Solution:
    def reorderSpaces(self, text: str) -> str:
        counter = 0
        i = 0
        j = 0
        word = []
        text += " "
        for k in range(len(text) - 1):
            if text[k] == " ":
                counter += 1
            if text[k] != " " and text[k - 1] == " ":
                i = k
            if text[k] != " " and text[k + 1] == " ":
                j = k
                if j >= i:
                    word.append(text[i:j + 1])
        if len(word) == 1:
            return str(word[0]) + counter * " "
        text = ""
        for i in range(len(word) - 1):
            text += word[i]
            text += " " * (counter // (len(word) - 1))
        text += word[-1]
        text += " " * (counter % (len(word) - 1))
        return text