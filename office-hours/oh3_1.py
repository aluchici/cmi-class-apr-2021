class A: 
    def add(self, a, b):
        return a + b + 'a'

class B(A):
    def add(self, a, b):
        return str(a + b) + 'b'

class C(B): 
    def add(self, a, b):
        return str(a + b) + 'c'

class D(B, C):
    pass

if __name__ == "__main__":
    c = C()
    c.add(1, 2)

    d = D()
    print(d.add(1, 1))