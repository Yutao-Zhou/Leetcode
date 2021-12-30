class Solution:
    def findComplement(self, num: int) -> int:
        #### loop and reverse, not real solution ####
        # num = list(bin(num))
        # for i in range(-1,-len(num),-1):
        #     if num[i] == "0":
        #         num[i] = "1"
        #     elif num[i] == "1":
        #         num[i] = "0"
        # num = int("".join(num),2)
        # return num