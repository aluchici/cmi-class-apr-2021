from functools import singledispatch
from multipledispatch import dispatch
from datetime import date, datetime, time

class A:
    pass 

def function_name(p1, p2):
    print(p1, p2)
    return p1 + p2

def f(r):
    if r == 1:
        return r
    return r + f(r-1) 

def fwithtypehints(a: int, b: float) -> float:
    return a + b

def fwithcustomtypehints(a: A) -> A:
    return a

# closure
def outside():
    msg = 'Hello %s'

    def inside(name):
        m = msg % name
        return m
    
    name = input('Enter name: ')
    m = inside(name)

    print(m)

def counter():
    count = 0

    def count1():
        nonlocal count 
        count += 1
        return count

    return count1

upper = lambda x: x.upper()

def transform(s, f):
    return f(s)

class B():
    def __init__(self, a, b=0):
        # y = a * x + b
        self.a = a
        self.b = b

    def __call__(self, x):
        return self.a * x + self.b

    @singledispatch
    def format(self, arg):
        return arg 

    @format.register
    def _(self, arg: date):
        return f"{arg.day}" 

# decorators
def uppercase_decorator(f):
    def wrapper():
        f1 = f()
        make_uppercase = f1.upper()
        return make_uppercase
    
    return wrapper

def split(f):
    def wrapper():
        f1 = f()
        s = f1.split()
        return s 

    return wrapper

def dec_with_args(f):
    def wrapper(p1, p2):
        print('p1: %s; p2: %s' % (p1, p2))
        return f(p1, p2)
    return wrapper

def decwithmultipleargs(f):
    def wrapper(*args, **kwargs):
        print('Inside wrapper')
        return f(*args, **kwargs)
    return wrapper

def dec_with_params(dp1, dp2):
    def decorator(f):
        def wrapper(fp1, fp2):
            print('f args: %s, %s \ndec args: %s, %s' % (fp1, fp2, dp1, dp2))
            return f(fp1, fp2)
        return wrapper
    return decorator


@split
@uppercase_decorator
def say_hello():
    return 'Hello world!'

@uppercase_decorator
def say_goodbye():
    return 'Bye'

@decwithmultipleargs
def fwitharglist(*args, **kwargs): 
    print(args)
    print(kwargs)

@dec_with_params(2, 3)
def fwith2args(p1, p2):
    print('Inside function with 2 args, p1: %s and p2: %s' % (p1, p2))

# operator overloading
# single dispatch 

@singledispatch
def format(arg):
    return arg 

@format.register
def _(arg: date):
    return f"{arg.day}-{arg.month}-{arg.year}"

@format.register
def _(arg: datetime):
    return f"{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}"

@format.register
def _(arg: time):
    return f"{arg.hour}:{arg.minute}:{arg.second}"

@dispatch(list, str)
def concatenate(a, b):
    a.append(b)
    return a

@dispatch(str, str)
def concatenate(a, b):
    return a + b 


if __name__ == '__main__':
    print(format('TEST'))
    print(format(date(2020, 10, 21)))
    print(format(datetime(2021, 5, 21, 10, 20)))
    print(format(time(1, 2, 40)))

    b = B(10, 20)
    print(b.format('TEST 2'))
    print(b.format(date(2020, 12, 20)))

    print(concatenate([1,2,3], 'a'))
    print(concatenate('string 1 + ', 'strint 2'))