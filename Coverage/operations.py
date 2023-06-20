import sys


#Fenix Kanat
def compute(a, b, operation):
    if operation == "subtract":
        return a - b
    if operation == "add":
        return a + b
    if operation == "multiply":
        return a * b



def compute2 (a,c, operation):
    if operation == "divide":
            return a / c


if __name__ == '__main__':

    input(compute(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))
