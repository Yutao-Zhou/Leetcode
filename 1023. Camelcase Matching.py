class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        #### Two Pointer ####
        ans = []
        for query in queries:
            j = 0
            for char in query:
                if 65 <= ord(char) <= 90:
                    if j < len(pattern) and pattern[j] == char:
                        j += 1
                    elif j == len(pattern) or (j < len(pattern) and pattern[j] != char):
                        j = -1
                        break
                elif j < len(pattern) and char == pattern[j]:
                        j += 1
            if j >= len(pattern):
                ans.append(True)
            else:
                ans.append(False)
        return ans