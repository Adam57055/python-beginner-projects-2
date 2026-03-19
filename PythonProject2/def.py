#Calculator
while True:
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    operator = input('Enter an operator:')
    if operator == '+':
        addition = num1+num2
        print(round(addition,2))
    elif operator == '-':
        subtraction = num1-num2
        print(round(subtraction,2))
    elif operator == '*':
        multiplication = num1*num2
        print(round(multiplication,2))
    elif operator == '/': #denominator cannot be zero
        if num2 != 0:
            division = num1/num2
            print(round(division,2))
        else:
            print('invalid number')
            continue #program reprompts user
    else:
        print('INVALID OPERATOR!')
        continue #program reprompts user
