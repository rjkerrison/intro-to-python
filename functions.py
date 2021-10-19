# big declarations
def say_hello(name):
    print(f"Hello, {name}!")


# lambdas are for small functions, written on the fly
add = lambda a, b: a + b

say_hello("Arjun")

print(add(5, 6))


def say_hello_to_robin_if_no_name_is_specified(name="Robin"):
    say_hello(name)


say_hello_to_robin_if_no_name_is_specified("Clem")
say_hello_to_robin_if_no_name_is_specified()
