class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            discount = prices[i]
            if i != len(prices) -1:
                for j in range(i+1 , len(prices)):
                    if prices[j] <= discount:
                        discount -= prices[j]
                        break
            res.append(discount)
        return res
