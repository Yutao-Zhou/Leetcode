class Solution:
    def average(self, salary: List[int]) -> float:
        mi = salary[0]
        mx = salary[0]
        c = 0
        for i in range(0,len(salary)):
            if salary[i] < mi:
                mi = salary[i]
            if salary[i] > mx:
                mx = salary[i]
        for i in range(0,len(salary)):
            if salary[i] == mi or salary[i] == mx:
                salary[i] = 0
                c += 1
        return sum(salary)/(len(salary) - c)