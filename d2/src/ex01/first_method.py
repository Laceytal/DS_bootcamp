class Research:
    def file_reader(self):
        with open("data.csv", 'r') as file:
            content = file.read()
            return(content)

if __name__ == "__main__":
    reader = Research()
    print(reader.file_reader())