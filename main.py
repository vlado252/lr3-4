# Запрашиваем у пользователя ввод первой стороны треугольника и сохраняем его в переменную a
a = float(input("Введи первую сторону:"))
# Запрашиваем у пользователя ввод второй стороны треугольника и сохраняем его в переменную b
b = float(input("Введи вторую сторону:"))
# Запрашиваем у пользователя ввод третьей стороны треугольника и сохраняем его в переменную c
c = float(input("Введи третью сторону:"))
# Проверяем, выполняется ли неравенство треугольника
if a > b + c or b > a + c or c > a + b:
    # Если одна из сторон больше суммы двух других, треугольник не существует
    print("Треугольник не существует")
else:
    # В противном случае треугольник существует
    print("Треугольник существует")
