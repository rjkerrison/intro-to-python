# Capitalise the first letter
is_this_python = True
is_this_javascript = False

if is_this_python or is_this_javascript:
    print("It is a programming language")

if is_this_python and is_this_javascript:
    print("It is a weird hybrid language, BEWARE")

a = 10
# ternary operators are a bit odd
# "b is 20 if a is less than 10 otherwise it's 40"
b = 20 if a < 10 else 40
print(b)
