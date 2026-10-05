from math import sqrt, exp, sin
x = float(input("Введите x: "))


def first_func(x):
    if x<1:
        y = x*(sin(x)**2)
        return y

def second_func(x):
    if x==1:
        y = sqrt(x**5+15)
        return y

def third_func(x):
    if x>1:
        y = exp(x)
        return y

def choise_func(x):
    if x < 1:
        res = first_func(x)
        print(res)
    if x == 1:
        res = second_func(x)
        print(res)
    if x > 1:
        res = third_func(x)
        print(res)

try:
    choise_func(x)

except OverflowError:
    print("Ошибка - мат функция не определена при данном x")