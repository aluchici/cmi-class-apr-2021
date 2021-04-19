a = 10
b = 20
c = a + b
print(a, b, c)

print(id(a), id(b))
print(id(c))

c = 50
print(c)
print(id(c))

l = [1, 2, 3]
m = l

print(id(l))
print(id(m))

m[0] = 'Teapa'
print(l)

def f(x):
    # x = x + 1
    x.append(2)
    print(x)
    if x:
        print(x)

print(l is m)
f(l)
print(l, m)


