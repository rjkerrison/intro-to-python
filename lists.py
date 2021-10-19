# Python is great at lists

# We can create ranges of numbers easily
numbers = range(10)
print(numbers)

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
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)
