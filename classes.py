# Classes in Python
class MyClass:
    # a constructor in python is the __init__ method
    def __init__(self):
        self.some_property = "some_value"
        self.count = 0

    # instance methods take 'self' as first param
    def add_to_count(self, num):
        self.count += num

    # static methods
    def default():
        return MyClass()


h = MyClass()

print(h.some_property)

h.add_to_count(4)
h.add_to_count(8)
h.add_to_count(15)
h.add_to_count(16)
h.add_to_count(23)
h.add_to_count(42)

print(h.count)

print(MyClass.default())
