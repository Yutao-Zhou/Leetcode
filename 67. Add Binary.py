class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #### digit by digit add ####
        # k = -1
        # ans = []
        # binary = ""
        # if len(a) <= len(b):
        #     for i in range(-1, -len(a) - 1, -1):
        #         ans.insert(0,(int(b[i]) + int(a[i])))
        #     for y in range(len(b) - len(a) - 1, -1, -1):
        #         ans.insert(0,int(b[y]))
        # if len(a) > len(b):
        #     for j in range(-1, -len(b) - 1, -1):
        #         ans.insert(0,(int(b[j]) + int(a[j])))
        #     for z in range(len(a) - len(b) - 1, -1, -1):
        #         ans.insert(0,int(a[z]))
        # while k >= -len(ans):
        #     if ans[k] > 1:
        #         if k == -len(ans):
        #             ans.insert(0,0)
        #         ans [k - 1] += 1
        #         if ans[k] == 2:
        #             ans[k] = 0
        #         else:
        #             ans[k] = 1
        #     k -= 1
        # for i in ans:
        #     binary += str(i)
        # return binary
    
        #### cheat fake solution ####
        # return str(bin(int(a,2) + int(b,2)))[2:]
        
        #### better digit by digit with carry ####
        carry = 0
        ans = ""
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            ans += str(carry % 2)
            carry //= 2
        return ans[::-1]