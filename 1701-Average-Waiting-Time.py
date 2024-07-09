class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        finish = 0
        tot_waiting = 0
        for c in customers:
            if finish > c[0]:
                waits = finish - c[0]
            else:
                waits = 0
            customer_wait = waits + c[1]
            finish = customer_wait + c[0]

            tot_waiting += customer_wait
        return tot_waiting / n
