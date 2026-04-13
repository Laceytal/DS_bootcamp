#!/usr/bin/env python3
import sys
import resource


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    flag=0
    if len(sys.argv) != 2:
        flag=1
    if flag==0:
        filepath = sys.argv[1]
        lines = read_file(filepath)

        for line in lines:
            pass
        usage = resource.getrusage(resource.RUSAGE_SELF)
        peak_memory_gb = usage.ru_maxrss / (1024 ** 2)  # в ГБ
        user_time = usage.ru_utime
        sys_time = usage.ru_stime

        print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
        print(f"User Mode Time + System Mode Time = {user_time + sys_time:.2f}s")

