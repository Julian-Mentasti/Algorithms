import math

def num_ways(n):
    head = 0
    counter = 0
    u = 0
    d = 0
    i = 0
    if (n == 0):
        return counter
    if (n%2 != 0):
        head = 1
    while (i*2-n-head != 0):
            u = (n - (2*i))
            d = i
            i += 1
            counter += math.factorial(u + d)/(math.factorial(u)*math.factorial(d))
    print(i * 2 - n - head)
    return counter + ((1 - head))

