import datetime

TODAY = datetime.datetime.now()

def sum(a, b):
    return a + b

if __name__ == "__main__":
    print('Today is: %s', TODAY)
    print('Sum of 2 and 3 is: %s', sum(2, 3))