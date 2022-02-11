class Binarysearchtree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binarysearchtree(data)
        else:
            #add data in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binarysearchtree(data)

    def inorder(self):
        elements = []

        if self.left:
            elements += self.left.inorder()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self):



def buildtree(elements):
    root = Binarysearchtree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildtree(numbers)
    # print(numbers_tree.inorder())
    print(numbers_tree.search(0))
    print(numbers_tree.find_max())