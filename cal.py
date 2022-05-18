def getOp(first, second):
    answer = 0
    op = input('enter the operation')
    if op == '+':
        answer = first + second
    elif op == '/' and second != 0:
        answer = first / second
    elif op == '-':
        answer = first - second
    elif op == '*':
        answer = first * second
    else:
        answer = 0
    return answer


def calculator():
    first = float(input("enter the first number"))
    second = float(input("Enter the second number"))
    answer = getOp(first, second)

    while True:
        ans = input("Are you done?\n1. Yes\n2. No\n")

        if ans == '1':
            break

        if ans == '2':
            first = answer
            second = float(input("enter the second number"))
            answer = getOp(first, second)

    return answer


print(calculator())