class Solution:
    def modifyString(self, s: str) -> str:
        # s = list(s)
        # r = 0
        # for i in range(len(s)):
        #     if s[i] == "?":
        #         r = randrange(97,123)
        #         while 1:
        #             if i != len(s) - 1:
        #                 if ord(s[i-1]) == r or ord(s[i+1]) == r:
        #                     r = randrange(97,123)
        #                 else:
        #                     break
        #             else:
        #                 if ord(s[i-1]) == r:
        #                     r = randrange(97,123)
        #                 else:
        #                     break
        #         s[i] = chr(r)
        # return s
        ck =  {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        ap = set()
        j = 0
        for i in s:
            if i != "?":
                ap.add(i)
        df = ck.difference(ap)
        df = list(df)
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                s[i] = df[j]
                if j < len(df) - 1:
                    j += 1
                else:
                    j -= 1
        return s