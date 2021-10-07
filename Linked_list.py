class Node:
    def __init__(self, a_value = None, b_value = None):
        self.a = a_value
        self.b = b_value


        self.link = None

    def print_values(self):
        print(self.a, self.b)


    def count_from_node(self):
        x = 0
        y = self


        for i in range(5):
            y.link = Node(i, i*3)
            y = y.link

            y.print_values()
            

        counter = 0
        while True:
            counter += 1
            y.print_values()
            y = y.link

            if y.link != None:
                y = y.link

            print(counter)



head = Node(5,6)
# head.print_values()
# print(head.a, head.b)
head.b = head.a + head.b
# print(head.a, head.b)

b = Node(56, 12)
# b.print_values()

head.link = b
# head.link.print_values()

c = Node(9, 0)
b.link = c
# b.link.print_values()


d = Node(2, 3)
d.link = head
# d.print_values()
# d.link.print_values()



# current = d
# for i in range(5):
#     current.link = Node(i, i*3)
#     current = current.link
#
#     current.print_values()


# current = d
# counter = 0
# while True:
#     counter += 1
#     current.print_values()
#     current = current.link
#
#     if current == None:
#         break
#
# print(counter)














