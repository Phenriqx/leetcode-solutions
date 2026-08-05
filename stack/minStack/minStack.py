class MinStack:
    def __init__(self):
        self.stack = []
        self.tracker = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.tracker and self.tracker[-1] < value:
            self.tracker.append(self.tracker[-1])
        else:
            self.tracker.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1]