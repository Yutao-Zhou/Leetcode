class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = {'q':-1,'w':-1,'e':-1,'r':-1,'t':-1,'y':-1,'u':-1,'i':-1,'o':-1,'p':-1,'Q':-1,'W':-1,'E':-1,'R':-1,'T':-1,'Y':-1,'U':-1,'I':-1,'O':-1,'P':-1}
        s = {'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'A':0,'S':0,'D':0,'F':0,'G':0,'H':0,'J':0,'K':0,'L':0}
        t = {'z':1,'x':1,'c':1,'v':1,'b':1,'n':1,'m':1,'Z':1,'X':1,'C':1,'V':1,'B':1,'N':1,'M':1}
        ans = []
        for i in words:
            if i[0] in f:
                for j in range(len(i)):
                    if i[j] in f and j == len(i)-1:
                        ans.append(i)
                    if i[j] not in f:
                        break
            if i[0] in s:
                for j in range(len(i)):
                    if i[j] in s and j == len(i)-1:
                        ans.append(i)
                    if i[j] not in s:
                        break
            if i[0] in t:
                for j in range(len(i)):
                    if i[j] in t and j == len(i)-1:
                        ans.append(i)
                    if i[j] not in t:
                        break
        return ans