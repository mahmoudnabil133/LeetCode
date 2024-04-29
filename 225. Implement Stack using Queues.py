class MyStack:

    def __init__(self):
        self.mylist = []

    def push(self, x: int) -> None:
        self.mylist.append(x)

    def pop(self) -> int:
        return self.mylist.pop()
        

    def top(self) -> int:
        return self.mylist[-1]

    def empty(self) -> bool:
        if len(self.mylist) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
