def fact(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a


for el in fact(10):
    print(el)