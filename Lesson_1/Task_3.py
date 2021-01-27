# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.
# hhttps://drive.google.com/file/d/1zjCdF5ZTABUqmMwkeLk06Lg9t-LYs9AC/view?usp=sharing

x1 = float(input("Введите координаты x1 для точки А: "))
y1 = float(input("Введите координаты y1 для точки A: "))

x2 = float(input("Введите координаты x2 для точки B: "))
y2 = float(input("Введите координаты y2 для точки B: "))
if x1 - x2 == 0:
    print("Уравнение не имеет решения!")
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    if b > 0:
        print(f"y = {k}x + {b}")
    else:
        print(f"y = {k}x - {abs(b)}")
