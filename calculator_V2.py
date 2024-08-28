n = float(input("please enter input numerical value: "))
while(True):
    opr = input("select '+' ; '-' ; '*' ; '/' ; '%' ; '=' ")

    if opr in ('+','-','*','/','%'):
        num = float(input("enter next number: "))

        if opr == '+':
            res = n+num

        elif opr == '-':
            res = n-num

        elif opr == '*':
            res = n*num

        elif opr == '/':
            if num == 0:
                print("Error: Division by zero")
                continue

            else:
                res = n/num

        elif opr == '%':
            res = n%num

        n=res

        print("Result: ", res)

    elif opr == '=':
        print("Result: ", res)
        break

    else:
        print("Invalid operator:")
        break