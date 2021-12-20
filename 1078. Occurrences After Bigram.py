class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        text = text.split(" ")
        for i in range(1,len(text) - 1):
            if text[i] == second:
                if text[i - 1] == first:
                    ans.append(text[i + 1])
        return ans