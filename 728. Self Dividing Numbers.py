class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        num = left
        while num <= right:
            if "0" in str(num):
                num += 1
            else:
                for i in range(len(str(num))):
                    if num % int(str(num)[i]) != 0:
                        break
                    elif i == len(str(num)) - 1:
                        ans.append(num)
                num += 1
        return ans