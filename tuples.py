# A tuple is a bit like a list, but you can't change it afterwards
# They're useful for grouping variables together, especially when returning from functions
tuple = (5, 6)

print(tuple)
print(tuple[0])
print(tuple[1])

_, b = tuple

print(b)


def find_sqrt(num):
    count = 0
    for i in range(1, num, 2):
        num -= i
        count += 1
        if num < 0:
            return (i, count)


print(find_sqrt(225))


basic_tuple = ("R", "o", "b", "i", "n")
# we cannot append
# basic_tuple.append(5)
# nor extend etc
# basic_tuple.extend([2, 3, 4])
# basic_tuple.remove(5)
# basic_tuple.insert(4, 178)

# we can access entries in a tuple
print(basic_tuple[1])
# we can deconstruct into new variables
r, o, b, i, n = basic_tuple
print(i)
print(n)
print(b)
print(o)
print(r)
