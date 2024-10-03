a = float(input("Введи первую сторону:"))
b = float(input("Введи вторую сторону:"))
c = float(input("Введи третью сторону:"))
if a > b+c or b > a+c or c > a+b:
    print("Треугольник не существует")
else:
    print("Треугольник существует")
