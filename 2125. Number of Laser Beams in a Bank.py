class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #### count and calculate ###
        ans = 0
        last = -1
        count = []
        for row in bank:
            counter = 0
            for place in row:
                if place == "1":
                    counter += 1
            count.append(counter)
        for n in count:
            if last == -1 and n != 0:
                last = n
            elif n != 0 and last != -1:
                ans += last * n
                last = n
        return ans