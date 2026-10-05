from math import sqrt, exp, sin
x = float(input("Введите x: "))


def func(x):
    y=0
    if x<1:
        y = x*(sin(x)**2)

    if x==1:
        y = sqrt(x**5+15)

    if x>1:
        y = exp(x)
    return y

try:
    print(func(x))

except OverflowError:
    print("Ошибка - мат функция не определена при данном x")