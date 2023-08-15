class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        ans = []
        i = 0
        search = ""
        for c in searchWord:
            tmp = []
            search = search + c
            while i < n and products[i] < search:
                i += 1
            for j in range(3):
                if i + j < n and len(products[i + j]) >= len(search) and products[i + j][:len(search)] == search:
                    tmp.append(products[i + j])
            ans.append(tmp)
        return ans