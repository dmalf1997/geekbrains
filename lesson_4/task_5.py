from functools import reduce

def summator(prev_el, el):
    return prev_el + el


print(reduce(summator, [i for i in range(100,1001) if i % 2 == 0]))
