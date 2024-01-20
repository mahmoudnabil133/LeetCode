class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next
        sum = 0
        mul = 1
        while st1 and st2:
            num1 = st1.pop() * mul
            num2 = st2.pop() * mul
            sum += num1 + num2
            mul *= 10
        if not st1:
            while st2:
                num2 = st2.pop() * mul
                sum +=num2
                mul *= 10
        elif not st2:
            while st1:
                num1 = st1.pop() * mul
                sum += num1
                mul *= 10
        prev = None
        current = None
        if not sum:
            current = ListNode(0)
        while sum:
            val = sum % 10
            sum //= 10
            current = ListNode(val)
            if not current:
                prev = current
                continue
            current.next = prev
            prev = current
        return current
