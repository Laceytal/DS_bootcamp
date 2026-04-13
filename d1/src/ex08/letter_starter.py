import sys

def letter_starter(email):
    input= open('employees.tsv','r')
    lines=input.readlines()
    for line in lines[1:]:
        if email in line:
            name = line.split('\t')[0]
            print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
            break
    input.close()

if __name__ == '__main__':
    letter_starter(sys.argv[1])