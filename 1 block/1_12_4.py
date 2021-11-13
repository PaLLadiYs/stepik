# calcualtor for 1_12 lesson ex.4
f = str(input())

if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    # calculator
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print(s)
if f == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
if f == 'круг':
    r = int(input())
    pi = 3.14
    print(r ** 2 * pi)