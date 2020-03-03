# Length check
def checklen(string):

    if len(string) % 3 == 0:
        print(f'Length case passed, length is:{len(string)}')
    else:
        print("Not good")

# atgc


def checkchar(c):
    if c == 'a' or c == 'A' or c == 't' or c == 'T' or c == 'g' or c == 'G' or c == 'c' or c == 'C':
        return True
    else:
        return False

# ending(stop)


def checkend(string):
    print(string[-3:])


class Nucleotides:
    def __init__(self, string):
        self.nucl = string


f1 = open("ip_test1.txt", "a")
string = ""
with open("Ecol_K12_MG1655_.wgs") as f:
    while True:

        s = f.read(1)

        if s == "":
            print("EOF")
            break
        if s == ">":
            next(f)
            continue
        if s == "\n":
            continue
        if checkchar(s):
            pass
        else:
            print('Gene sequence has invalid character:', s)
            break

        string += s

# f1.write(string)
checklen(string)
f1.close()

# print(string)
print(len(string))
# print('First 10:', string[0:11])
checkend(string)
