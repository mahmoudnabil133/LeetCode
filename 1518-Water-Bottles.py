class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrinked, currentEmpty = numBottles, numBottles
        while currentEmpty >= numExchange:
            exchanged = int(currentEmpty / numExchange)
            totalDrinked += exchanged
            remaining = currentEmpty - (exchanged * numExchange)
            currentEmpty = exchanged + remaining
        return totalDrinked