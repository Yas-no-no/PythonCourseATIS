import os

data = input('Введите имя: ')
os.system('echo data') #не соображу как сделать чтобы переменная передавала значение в функцию систем

#либо нужно было сделать проще, примерно та
name = input('Введите имя: ')
print('"Echo:"', name)