import os
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as file:
            content = file.readlines()

        if has_header:
            header = content[0].strip().split(',')
            if len(header) != 2 or not header[0].isalpha() or not header[1].isalpha():
                raise ValueError('Incorrect Header in file')
            content = content[1:]

        data = []
        for line in content:
            first, second = line.strip().split(',')
            if int(first) not in (0, 1) or int(second) not in (0, 1) or first == second:
                raise ValueError('Incorrect data in file')
            data.append([int(first), int(second)])

        return data

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return heads / total * 100, tails / total * 100

    class Analytics(Calculations):
        def predict_random(self, steps):
            result = []
            for _ in range(steps):
                if randint(0, 1) == 0:
                    result.append([0, 1])
                else:
                    result.append([1, 0])
            return result

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, filename, ext):
            if not isinstance(data, str):
                raise ValueError("Data for saving must be a string")
            path = f"{filename}.{ext}"
            with open(path, "w") as f:
                f.write(data)
            return os.path.abspath(path)


