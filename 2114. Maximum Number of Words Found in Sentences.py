class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        #### find space one pass ####
        # cache = 1
        # ans = 1
        # for i in sentences:
        #     for j in i:
        #         if j == " ":
        #             cache += 1
        #     if cache > ans:
        #         ans = cache
        #     cache = 1
        # return ans
        
        #### one liner ####
        return max(sentence.count(" ")for sentence in sentences) + 1