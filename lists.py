# Python is great at lists

# We can create ranges of numbers easily
numbers = range(10)
print(numbers)

for i in numbers:
    print(f"i is {i}")

# What the hell is this thing?
# It's called a list comprehension!
# This builds an array from the range.
numbers = [x for x in numbers]
print(numbers)

# We can operate during comprehensions.
# This maps the range.
numbers_squared = [x ** 2 for x in numbers]
print(numbers_squared)

# We can even filter with them
# in pseudocode terms, this list is "x squared for x in numbers if x is even"
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)


basic_list = [1, 2, 3]
# for adding an extra item
basic_list.append(5)
# for adding an extra array
basic_list.extend([2, 3, 4])
print(basic_list)
basic_list.remove(5)
print(basic_list)
basic_list.insert(4, 178)
print(basic_list)
