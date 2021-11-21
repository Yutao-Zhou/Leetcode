class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ####really doing it########
        ck = []
        for i in range(len(emails)):
            emails[i] = emails[i].split("@")
            emails[i][0] = emails[i][0].split("+")
            emails[i][0] = emails[i][0][0]
            emails[i][0] = emails[i][0].replace(".","")
            emails[i] = "@".join(emails[i])
        for i in emails:
            if i not in ck:
                ck.append(i)
        return len(ck)