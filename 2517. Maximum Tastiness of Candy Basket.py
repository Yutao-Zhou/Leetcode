class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        l, r = 0, price[-1] - price[0]
        while l < r:
            mid = (l + r + 1) // 2
            bucket = 1
            last_candy = price[0]
            for p in price:
                if p - last_candy >= mid:
                    last_candy = p
                    bucket += 1
            if bucket >= k:
                l = mid
            else:
                r = mid - 1  
        return l