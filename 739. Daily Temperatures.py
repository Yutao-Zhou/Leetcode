class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #### Brute force with dancing two pointers ####
        # ans = []
        # l = len(temperatures)
        # for i in range(l - 1):
        #     counter = 0
        #     for j in range(i + 1, l):
        #         counter += 1
        #         if temperatures[i] < temperatures[j]:
        #             ans.append(counter)
        #             break
        #         elif j == l - 1:
        #             ans.append(0)
        # ans.append(0)
        # return ans
        
        #### Smater two pointers ####
        # l, rightMax = len(temperatures), float('-inf')
        # ans = [0] * l
        # for i in range(l - 1, -1, -1):
        #     if temperatures[i] >= rightMax:
        #         rightMax = temperatures[i]
        #     else:
        #         counter = 1
        #         while temperatures[i + counter] <= temperatures[i]:
        #             counter += ans[i + counter]
        #         ans[i] = counter
        # return ans
        
        #### Stack ####
        l = len(temperatures)
        ans = [0] * l
        stack = []
        for i in range(l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans