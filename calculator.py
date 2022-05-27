def addition(f_number, s_number):
    count= f_number+s_number
    print(count)

def subtraction(f_number,s_number):
    count = f_number - s_number
    print(count)


def multiplication(f_number,s_number):
    count = f_number * s_number
    print(count)

def modulus(f_number, s_number):
    count = f_number % s_number
    print(count)

def division(f_number, s_number):
    count = f_number / s_number
    print(count)

def initially():
    f_number = int(input("Please state the first number to input:\t"))
    s_number = int(input("Please state the first number to input:\t"))
    process = str(input("Please process to perform, multiplication, addition, subtraction, modulus, division:\t")).lower()
    if process == "multiplication":
        addition(f_number, s_number)
    elif process == "subtraction":
        subtraction(f_number, s_number)
    elif process == "division":
        division(f_number, s_number)
    elif process == "addition":
        modulus(f_number, s_number)
    else:
        multiplication(f_number, s_number)
    # multiplication(Nlist)

if __name__ == '__main__':
    initially()