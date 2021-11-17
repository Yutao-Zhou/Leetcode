str2index = {"type":0,"color":1,"name":2}

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        ans = 0
        for item in items:
            if item[str2index[ruleKey]] == ruleValue:
                ans += 1
        return ans