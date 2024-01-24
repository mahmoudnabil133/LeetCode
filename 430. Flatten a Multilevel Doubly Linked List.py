
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        arr = []
        arr = self.Iterate(head, arr)
        if arr:
            Prev = Node(arr[0], None, None, None)
            Head = Prev
            for i in range(1, len(arr), 1):
                current = Node(arr[i], Prev, None, None)
                current.prev.next = current
                Prev = current
            return Head
        else:
            return None
    def Iterate(self,head, arr):
        if not head:
            return None
        while head:
            if head.child:
                arr.append(head.val)
                son = head.child
                head = head.next
                self.Iterate(son, arr)
            else:
                arr.append(head.val)
                head = head.next
        return arr
