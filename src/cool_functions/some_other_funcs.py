def sum_up(l):
    sum = 0
    for item in l:
        sum += item
    return sum

def factorial(N):
    assert isinstance(N, int)
    assert N >= 0
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)

def difference(a,b):
    return a-b