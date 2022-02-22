class Empty(Exception):
    pass


class Stack:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def display(self):
        print(self.data)


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 10):
        stack.push(i)
    stack.display()
    stack.pop()
    stack.pop()
    stack.display()


