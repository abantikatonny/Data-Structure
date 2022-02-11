# array(data_type, value list)
import array as arr

# creating an array
a = arr.array("i", [1, 2, 3])

for i in range(0, 3):
    print(a[i])
    print(a)

# insert element
a.insert(1, 10)
print(a)

# append
a.append(9)
print(a)

# remove
a.remove(9)
print(a)

# list create blank
p = []
print(p)
# create list with int
p = [1, 2, 3]
print(p)
# create list with multi types
p = [1, 3, "value", "i", 6]