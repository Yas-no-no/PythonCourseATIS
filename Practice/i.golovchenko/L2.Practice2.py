def return_max(a, b):
    if a >= b:
        return a
    else:
        return b


num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))
print(return_max(num1, num2))
