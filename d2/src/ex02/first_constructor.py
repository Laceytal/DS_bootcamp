import sys

class Research:
    def __init__(self, path):
        self.path = path
    def file_reader(self):
        with open(path, 'r') as file:
            content = file.readlines()
            header = content[0].strip().split(',')
            if len(header) != 2 or not header[0].isalpha() or not header[1].isalpha():
                raise ValueError('Incorrect Header in file')
            for line in content[1:]:
                first, second = line.strip().split(',')
                if int(first) not in (0,1) or int(second) not in (0,1) or first==second:
                    raise ValueError('Incorrect data in file')
            return ''.join(content)


if __name__ == "__main__":
    path = sys.argv[1]
    reader = Research(path)
    print(reader.file_reader())