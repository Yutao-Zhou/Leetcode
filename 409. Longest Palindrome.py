class Solution:
    def longestPalindrome(self, s: str) -> int:
        #### count and creat ####
        ans = 0
        resource = {}
        for l in s:
            if l in resource:
                resource[l] += 1
            if l not in resource:
                resource[l] = 1
        freq = sorted(resource.values(), reverse = True)
        for n in freq:
            if n % 2 == 0:
                ans += n
            else:
                if ans % 2 == 1:
                    ans += n - 1
                else:
                    ans += n
        return ans