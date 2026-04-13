#!/usr/bin/env python3
import sys
import timeit
from functools import reduce


def sum_loop(n):
    result = 0
    for i in range(1, n + 1):
        result += i*i
    return result

def sum_reduce(n):
    return reduce(lambda acc, x: acc + x*x, range(1, n+1), 0)

if __name__ == "__main__":
    FUNCTIONS = {
        "loop": sum_loop,
        "reduce": sum_reduce
    }

    flag=0
    if len(sys.argv) != 4:
        flag=1
    if flag==0:
        func_name = sys.argv[1]
        number = int(sys.argv[2])
        n = int(sys.argv[3])

        if func_name not in FUNCTIONS:
            flag = 1
        if flag == 0:
            func = FUNCTIONS[func_name]
            elapsed = timeit.timeit(lambda: func(n), number=number)
            print(elapsed)
