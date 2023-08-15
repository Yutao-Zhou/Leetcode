class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        len_weights = len(weights)
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            d, cur_weight = 1, 0
            for weight in weights:
                cur_weight += weight
                if cur_weight > mid:
                    d += 1
                    cur_weight = weight
            if d > days:
                l = mid + 1
            else:
                r = mid
        return l