# Last updated: 3/22/2026, 12:45:48 AM
class MyStack:

    def __init__(self):
        self.l = []
        

    def push(self, x: int) -> None:
        self.l.append(x)
        

    def pop(self) -> int:
        if(len(self.l)==0):
            return -1
        return self.l.pop()

    def top(self) -> int:
        return self.l[-1]
        

    def empty(self) -> bool:
        if not self.l:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()