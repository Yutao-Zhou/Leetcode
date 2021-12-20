class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for letter in s:
            width += widths[ord(letter) - 97]
            if width > 100:
                width = widths[ord(letter) - 97]
                lines += 1
        return [lines,width]