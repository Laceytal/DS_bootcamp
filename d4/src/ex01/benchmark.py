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

def filter_map(emails):
    return list(filter(None, map(lambda e: e if e.endswith('@gmail.com') else None, emails)))

if __name__ == "__main__":
    emails = [
                 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
                 'anna@live.com', 'philipp@gmail.com'
             ] * 5
    loop_time = timeit.timeit(lambda: filter_loop(emails), number=90_000_000)
    comp_time = timeit.timeit(lambda: filter_list_comprehension(emails), number=90_000_000)
    map_time = timeit.timeit(lambda: filter_map(emails), number=90_000_000)
    best_time = min(loop_time, comp_time, map_time)
    if best_time == loop_time:
        print("It is better to use a loop")
    elif best_time == comp_time:
        print("It is better to use a list comprehension")
    else:
        print("it is better to use a map")

    times_sorted = sorted([
        ("loop", loop_time),
        ("list comprehension", comp_time),
        ("map", map_time)
    ], key=lambda x: x[1])

    print(" vs ".join(str(t[1]) for t in times_sorted))
