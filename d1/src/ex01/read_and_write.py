def read_and_write():
    input = open('ds.csv', 'r')
    output = open('ds.tsv', 'w')
    text = input.read()
    words = text.split(',')
    for word in words:
        if word[1] =='"' or word[len(word) - 1] == '"' or word=="false" or word=="true":
            output.write(word)
            output.write('\t')
        else:
            output.write(word)
    input.close()
    output.close()
if __name__ == '__main__':
    read_and_write()