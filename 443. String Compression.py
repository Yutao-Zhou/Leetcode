class Solution:
    def compress(self, chars: List[str]) -> int:
        #### Brute Force Two pointers ####
        slow, fast, l = 0, 0, len(chars)
        while fast < l:
            counter = 1
            while fast + 1 < l and chars[fast] == chars[fast + 1]:
                fast += 1
                counter += 1
            chars[slow] = chars[fast]
            if counter > 1:
                for c in str(counter):
                    slow += 1
                    chars[slow] = c
            slow += 1
            fast += 1
        return slow