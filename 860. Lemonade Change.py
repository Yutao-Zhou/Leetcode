class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                change[5] += 1
            if bills[i] == 10:
                change[10] += 1
                change[5] -= 1
            if bills[i] == 20:
                if change[10] == 0:
                    change[5] -= 3
                if change[10] > 0:
                    change[20] += 1
                    change[10] -= 1
                    change[5] -= 1
            if change[5] < 0 or change[10] < 0 or change[20] < 0:
                return False
        return True