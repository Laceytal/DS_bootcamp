#!/usr/bin/env python3
import sys
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

def filter_filter(emails):
    return list(filter(lambda e: e.endswith('@gmail.com'), emails))

if __name__ == "__main__":
    FUNCTIONS = {
        "loop": filter_loop,
        "list_comprehension": filter_list_comprehension,
        "map": filter_map,
        "filter": filter_filter,
    }
    emails = [
                 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
                 'anna@live.com', 'philipp@gmail.com'
             ] * 5
    flag=0
    if len(sys.argv) != 3:
        flag=1
    if flag==0:
        func_name = sys.argv[1]
        number = int(sys.argv[2])

        if func_name not in FUNCTIONS:
            flag=1
        if flag==0:
            func = FUNCTIONS[func_name]
            elapsed = timeit.timeit(lambda: func(emails), number=number)
            print(elapsed)
