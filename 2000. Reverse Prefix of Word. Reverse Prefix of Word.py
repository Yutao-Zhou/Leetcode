class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        j = 0
        k = 0
        if ch not in word:
            return word
        else:
            word = list(word)
            for k in range(len(word)):
                if word[k] == ch:
                    j = k
                    break
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            return "".join(word)