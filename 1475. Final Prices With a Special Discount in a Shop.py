class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0,len(prices),1):
            for j in range(0,len(prices),1):
                if prices[i] >= prices[j] and i < j:
                    prices [i] -= prices[j]
                    break
                else:
                    pass
        return prices