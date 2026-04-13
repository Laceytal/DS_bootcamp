#!/usr/bin/env python3
import timeit
import random
from collections import Counter

numbers = [random.randint(0, 100) for _ in range(1_000_000)]

def count_numbers_manual(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

def top_10_manual(lst):
    count_dict = count_numbers_manual(lst)
    top_10 = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:10])
    return top_10

def count_numbers_counter(lst):
    return Counter(lst)

def top_10_counter(lst):
    return dict(Counter(lst).most_common(10))

if __name__ == '__main__':
    my_count_time = timeit.timeit(lambda: count_numbers_manual(numbers), number=1)
    counter_count_time = timeit.timeit(lambda: count_numbers_counter(numbers), number=1)
    my_top_time = timeit.timeit(lambda: top_10_manual(numbers), number=1)
    counter_top_time = timeit.timeit(lambda: top_10_counter(numbers), number=1)

    print(f"my function: {my_count_time:.7f}")
    print(f"Counter: {counter_count_time:.7f}")
    print(f"my top: {my_top_time:.7f}")
    print(f"Counter's top: {counter_top_time:.7f}")
