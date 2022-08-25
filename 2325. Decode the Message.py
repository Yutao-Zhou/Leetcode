class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        #### Creat hashtabe and convert ####
        ans, counter, hashtable = "", 0, {" ": " "}
        for c in key:
            if c not in hashtable:
                hashtable[c] = chr(97 + counter)
                counter += 1
        for c in message:
            ans = ans + hashtable[c]
        return ans