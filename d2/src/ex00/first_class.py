class Must_Read:
    with open("data.csv", 'r') as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    reader = Must_Read()