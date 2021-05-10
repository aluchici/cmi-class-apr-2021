# Sample code transforming a class into a sequence type (partial implementation).
# def it():
#     days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for d in days:
#         yield d

# for i in it():
#     print(i)

class C:
    def __init__(self):
        self.L = [1, 2, 3, 4, 5, 6, 7]

    def __iter__(self):
        for i in self.L:
            yield i

    def __getitem__(self, k):
        return self.L[k]

    def __setitem__(self, k, val):
        self.L[k] = val

c = C()
for ci in c:
    print(ci)

print(c[1])
c[1] = 10
print(c[1])

print(c[1:3])

d = c[1:3]
print(d[0])
d[0] = 60
print(c[1])
print(d[0])