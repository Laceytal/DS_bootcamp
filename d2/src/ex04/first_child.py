import sys
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

if __name__ == "__main__":
    path = sys.argv[1]
    reader = Research(path)

    data = reader.file_reader()
    print(data)

    analytics = Research.Analytics(data)

    heads, tails = analytics.counts()
    print(heads, tails)

    frac_heads, frac_tails = analytics.fractions(heads, tails)
    print(frac_heads, frac_tails)

    print(analytics.predict_random(3))
    print(analytics.predict_last())
