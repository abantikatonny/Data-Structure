"""for understanding the concept : https://www.youtube.com/watch?v=T_UXDTy23DQ&t=27s&ab_channel=Jenny%27slecturesCS%2FITNET%26JRF """
""""https://www.geeksforgeeks.org/stack-in-python/"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        poppednode = self.head
        self.head = self.head.next
        poppednode.next = None
        return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        tempnode = self.head
        if self.isempty():
            print("stack underflow")
        else:
            while (tempnode!= None):
                print(tempnode.data, "--->", end = " ")
                tempnode = tempnode.next
            return


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.display()
stack.pop()
print("\nNew list", stack.peek())
stack.display()






