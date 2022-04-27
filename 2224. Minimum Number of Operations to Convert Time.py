    class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        #### greedy recursion ####
        # current = current.split(":")
        # for i in range(len(current)):
        #     current[i] = int(current[i])
        # correct = correct.split(":")
        # for i in range(len(correct)):
        #     correct[i] = int(correct[i])
        # if correct[1] < current[1]:
        #     correct[1] += 60
        #     correct[0] -= 1
        # def recusion(current, ans):
        #     if current == correct:
        #         return ans
        #     if current[0] < correct[0]:
        #         return recusion([current[0] + 1, current[1]], ans + 1)
        #     if correct[1] - current[1] >= 15:
        #         return recusion([current[0], current[1] + 15], ans + 1)
        #     if correct[1] - current[1] >= 5:
        #         return recusion([current[0], current[1] + 5], ans + 1)
        #     if correct[1] - current[1] >= 1:
        #         return recusion([current[0], current[1] + 1], ans + 1)
        # return recusion(current, 0)
    
        #### greedy iteritive ####
        ans = 0
        current = current.split(":")
        for i in range(len(current)):
            current[i] = int(current[i])
        correct = correct.split(":")
        for i in range(len(correct)):
            correct[i] = int(correct[i])
        if correct[1] < current[1]:
            correct[1] += 60
            correct[0] -= 1
        while current != correct:
            if current[0] < correct[0]:
                current[0] += 1
                ans += 1
            elif correct[1] - current[1] >= 15:
                current[1] += 15
                ans += 1
            elif correct[1] - current[1] >= 5:
                current[1] += 5
                ans += 1
            elif correct[1] - current[1] >= 1:
                current[1] += 1
                ans += 1
        return ans