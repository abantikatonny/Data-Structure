from random import randint


class Node:
    def __init__(self, a_value=None, b_value=None):
        self.a = a_value
        self.b = b_value

        self.link = None

    def print_values(self):
        print(self.a, self.b)

    def count_from_node(self):
        x = 0
        y = self

        counter = 0
        while True:
            counter += 1
            y.print_values()
            y = y.link

            if y == None:
                break

        print(counter)
        return counter


def auto_generate_nodes(L):
    """
    Given the expected length L, this function will create a linked list of length L and return the head.

    Parameters:
    ----------
    L: the expected length of linked list.

    Return:
    -------
    The head of a linked list of length L.

    """

    head = Node(6, 8)
    last = head

    for i in range(L-1):
        last.link = Node(i+1, 8)
        last = last.link

    return head



# head = Node(5, 6)
# # head.print_values()
# # print(head.a, head.b)
# head.b = head.a + head.b
# # print(head.a, head.b)
#
# b = Node(56, 12)
# # b.print_values()
#
# head.link = b
# # head.link.print_values()
#
# c = Node(9, 0)
# b.link = c
# # b.link.print_values()
#
#
# d = Node(2, 3)
# d.link = head
# # d.print_values()
# # d.link.print_values()
# # d.count_from_node()
# d.auto_generate_nodes()

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


x = auto_generate_nodes(10)
x.print_values()
x.count_from_node()
