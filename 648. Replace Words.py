class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #### simulation ####
        dictionary = sorted(dictionary, key = len)
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            for root in dictionary:
                if root in sentence[i][:len(root)]:
                    sentence[i] = root
                    break
        return " ".join(sentence)