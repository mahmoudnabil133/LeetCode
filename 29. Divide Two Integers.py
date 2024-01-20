class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos_edge = 2147483647
        neg_edge = -2147483648

        x = (dividend / divisor)
        x = int(x)
        if x > pos_edge:
            return pos_edge
        elif x < neg_edge:
            return neg_edge
        return x
