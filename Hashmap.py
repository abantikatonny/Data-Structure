class Node:
    # constructor to initialize the data and the next field for a node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("empty")
            return
        itr = self.head
        nwstr = ""

        while itr:
            nwstr += str(itr.data) + "---->"
            itr = itr.next
        print(nwstr)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.print()





