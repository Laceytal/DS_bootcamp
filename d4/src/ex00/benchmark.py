#!/usr/bin/env python3
import timeit

def filter_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result

def filter_list_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

if __name__ == "__main__":
    emails = [
                 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
                 'anna@live.com', 'philipp@gmail.com'
             ] * 5
    loop_time = timeit.timeit(lambda: filter_loop(emails), number=90_000_000)
    comp_time = timeit.timeit(lambda: filter_list_comprehension(emails), number=90_000_000)

    if comp_time <= loop_time:
        print("It is better to use a list comprehension")
    else:
        print("It is better to use a loop")
    times_sorted = sorted([("list comprehension", comp_time), ("loop", loop_time)], key=lambda x: x[1])
    print(f"{times_sorted[0][1]} vs {times_sorted[1][1]}")
