class MyQueue:

    def __init__(self):
        self.mylist = []

    def push(self, x: int) -> None:
        self.mylist.insert(0, x)

    def pop(self) -> int:
        return self.mylist.pop()

    def peek(self) -> int:
        return self.mylist[-1]
        
    def empty(self) -> bool:
        if len(self.mylist) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
