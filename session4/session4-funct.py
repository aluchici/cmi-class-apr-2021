def factorial(n):
    if n <= 2:
        return n 

    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact 

a = [1, 2, 3, 4, 5]
mapped_a = map(factorial, a)
print(mapped_a)
# list_mapped_a = list(mapped_a)
# print(list_mapped_a)

# for el in mapped_a:
#     print(el)

f = lambda x: x if x > 3 else None

b = filter(f, a)
c = list(b)
print(c)

g = [0, 0, 0, 0, 10, 10]
d = filter(lambda x: x == 0, g)
e = list(d)
print(e)

h = filter(lambda x: x < 5, map(lambda x: x * 2, a))
i = list(h)
print(i)

def j(*args):
    print(args)
    print(args[1])
    print(args[3] * 2)

j(1,3,45,6,7,8)
j(12,32)

