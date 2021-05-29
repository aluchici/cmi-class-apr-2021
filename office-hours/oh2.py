def f(x):
    
    def g(y):
        return x + y
    
    return g(2)

print(f(3))

class A:
    """
    Acesta e un docstring.
    """
    def __init__(self):
        self.a = None

    def my_method(self, x):
        self.a = x

from pprint import pprint
pprint(A.__dict__)




