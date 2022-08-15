class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #### All situation ####
        x, y = 0, 0
        if ax1 <= bx1 <= ax2:
            if ax1 <= bx2 <= ax2:
                x = bx2 - bx1
            else:
                x = ax2 - bx1
        if ax1 <= bx2 <= ax2:
            if ax1 <= bx1 <= ax2:
                x = bx2 - bx1
            else:
                x = bx2 - ax1
        if bx1 < ax1 and bx2 > ax2:
            x = ax2 - ax1
        if ay1 <= by1 <= ay2:
            if ay1 <= by2 <= ay2:
                y = by2 - by1
            else:
                y = ay2 - by1
        if ay1 <= by2 <= ay2:
            if ay1 <= by1 <= ay2:
                y = by2 - by1
            else:
                y = by2 - ay1
        if by1 < ay1 and by2 > ay2:
            y = ay2 - ay1
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - x * y