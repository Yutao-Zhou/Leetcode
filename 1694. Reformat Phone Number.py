class Solution:
    def reformatNumber(self, number: str) -> str:
        ##### ugly solution #####
        # numbers = []
        # j = 0
        # ans = ""
        # cache = []
        # for i in number:
        #     if ord("0") <= ord(i) <= ord("9"):
        #         numbers.append(i)
        # if len(numbers) < 4:
        #     return "".join(numbers)
        # if len(numbers) == 4:
        #     ans += numbers[-4]
        #     ans += numbers[-3]
        #     ans += "-"
        #     ans += numbers[-2]
        #     ans += numbers[-1]
        #     return ans
        # while 1:
        #     cache = numbers[3 * j: 3 * (j + 1)]
        #     for i in cache:
        #         ans += str(i)
        #     if len(numbers) - 3 * (j + 1) == 0:
        #         return ans
        #     ans += "-"
        #     if len(numbers) - 3 * (j + 1) == 4:
        #         ans += numbers[-4]
        #         ans += numbers[-3]
        #         ans += "-"
        #         ans += numbers[-2]
        #         ans += numbers[-1]
        #         return ans
        #     if len(numbers) - 3 * (j + 1) == 2:
        #         ans += numbers[-2]
        #         ans += numbers[-1]
        #         return ans
        #     j += 1
        
        ###### same logic better solution #####
        ans = ""
        counter = 0
        cache = []
        for i in range(len(number)):
            if ord("0") <= ord(number[i]) <= ord("9"):
                ans += number[i]
                counter += 1
                cache.append(number[i])
            if counter == 3 and i != len(number) - 1:
                ans += "-"
                counter = 0
            if counter == 1 and i == len(number) - 1:
                ans = ans[:len(ans) - 3]
                ans += "-"
                ans += cache[-2]
                ans += cache[-1]
        if ans[-1] == "-":
            return ans[:len(ans) - 1]
        else:
            return ans