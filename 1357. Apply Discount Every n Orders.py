class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.num_customer = 0
        self.price_dic = {}
        for i in range(len(products)):
            self.price_dic[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        self.num_customer += 1
        for i in range(len(product)):
            total += self.price_dic[product[i]] * amount[i]
        if not self.num_customer % self.n:
            total *= ((100 - self.discount) / 100)
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)