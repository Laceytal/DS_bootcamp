#!/usr/bin/env python3
import sys
import resource


def read_file_generator(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    filepath = sys.argv[1]
    for line in read_file_generator(filepath):
        pass
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory_gb = usage.ru_maxrss / (1024 ** 2)  # в ГБ
    user_time = usage.ru_utime
    sys_time = usage.ru_stime
    print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {user_time + sys_time:.2f}s")
