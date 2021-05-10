def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n-1)


def _max(a, index, l):
    local_max = -1

    if index >= l - 2:
        if a[index] > a[index + 1]: 
            return a[index]
        else:
            return a[index+1]

    local_max = _max(a, index + 1, l)

    if a[index] > local_max:
        return a[index]
    else:
        return local_max

def _min(a, index, l):
    local_min = 99999
    if index >= l - 2:
        if a[index] < a[index + 1]:
            return a[index]
        else:
            return a[index + 1]

    local_min = _min(a, index + 1, l)

    if a[index] < local_min:
        return a[index]
    else:
        return local_min

def partition(start, end, array):
    pivot_index = start 
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        
        while array[end] > pivot:
            end -= 1
    
        if start < end:
            # array[start], array[end] = array[end], array[start]
            k = array[start]
            array[start] = array[end]
            array[end] = k
    
    k = array[end]
    array[end] = array[pivot_index]
    array[pivot_index] = k

    return end

def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)

        quick_sort(start, p-1, array)
        quick_sort(p+1, end, array)

# Fractional greedy
class ItemValue:

    def __init__(self, w, val, ind):
        self.w = w
        self.val = val
        self.ind = ind
        self.cost = val // w 

    def __lt__(self, other):
        return self.cost < other.cost 

class FractionalKnapSack:

    @staticmethod
    def getMaxValue(w, val, capacity):
        ival = []

        for i in range(len(w)):
            ival.append(ItemValue(w[i], val[i], i))
        
        ival.sort(reverse=True)

        total_value = 0
        for i in ival:
            crt_w = int(i.w)
            crt_val = int(i.val)
            
            if capacity - crt_w >= 0:
                capacity -= crt_w
                total_value += crt_val
            else:
                fraction = capacity / crt_w
                total_value += crt_val * fraction
                capacity = int(capacity - crt_w * fraction)
                break
        return total_value



if __name__ == "__main__":
    a = [10, 24, 210, 4, 12, 2392, 21, 120, 21] # 9
    print(_max(a, 0, len(a)))
    print(_min(a, 0, len(a)))

    b = [1, 2, 3, 4]
    print(b)
    quick_sort(0, len(b)-1, b)
    print(b)

    a, b, c = 1, 2, 4
    print(a, b, c)


    w = [10, 200, 20, 58, 178]
    val = [1000, 100, 1, 500, 462]
    capacity = 10

    print(FractionalKnapSack.getMaxValue(w, val, capacity))
