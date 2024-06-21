class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sad_customers = 0
        l = 0
        for r in range(minutes):
            sad_customers += customers[r] * grumpy[r]
        
        max_sad_customers = sad_customers
        
        for r in range(minutes, len(customers)):
            sad_customers -= customers[l] * grumpy[l]
            sad_customers += customers[r] * grumpy[r]
            l += 1
            max_sad_customers = max(max_sad_customers, sad_customers)
        
        # could be satisfied
        satisfied = max_sad_customers
        for i in range(len(customers)):
            satisfied += customers[i] * (1- grumpy[i])
        return satisfied