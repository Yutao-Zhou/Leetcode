class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        c = 0
        ans = [0]*num_people
        i = 0
        while 1:
            if candies <= 0:
                return ans
            if candies <= c:
                if i == len(ans):
                    ans[0] += candies
                    return ans
                else:
                    ans[i] += candies
                    return ans
            if i == len(ans)-1:
                c += 1
                ans[i] += c
                candies -= c
                i = 0
            else:
                c += 1
                ans[i] += c
                candies -= c
                i += 1
        print(candies, ans)