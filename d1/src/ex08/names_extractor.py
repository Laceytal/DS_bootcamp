import sys

def names_extractor(path):
    input=open(path,'r')
    output=open('employees.tsv','w')
    output.write("Name\tSurname\tE-mail\n")
    lines=input.readlines()
    for line in lines:
        email=line
        tmp1=line.split('.',2)
        name = tmp1[0].capitalize()
        surname = tmp1[1].split('@')[0].capitalize()
        output.write(f"{name}\t{surname}\t{email}")
    input.close()
    output.close()

if __name__ == '__main__':
    names_extractor(sys.argv[1])