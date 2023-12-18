"""
(mediam problem)

linked list problem
first iterate 2 linked lists to aptain the 2 numbers and add them
then separate each digit of the number and append it to list
then create a linked list and return.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        mul = 1
        output = []
        while l1 != None:
           x = l1.val
           num1 += (x * mul)
           mul *= 10
           l1 = l1.next
        mul = 1
        while l2 != None:
           x = l2.val
           num2 += (x * mul)
           mul *= 10
           l2 = l2.next
        sum = num1 + num2
        while sum:
            a = sum % 10
            output.append(a)
            sum /= 10
        if not sum:
            current = ListNode(0)
        # output = output.reverse()
        if len(output):
            current = ListNode(output[len(output) - 1])
            for x in range(len(output) - 2, -1, -1):
                node = ListNode(output[x])
                node.next = current
                current = node

        return current           
        