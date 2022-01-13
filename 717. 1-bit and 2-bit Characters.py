class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        for i in range(-2, -len(bits) - 1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        return count % 2 == 0