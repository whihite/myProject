from math import sin, cos
while True:
    x = (input("Введите x:\n "))
    if not x.isdigit():
        print ("Вы ввели букву, а надо цифру: ")
    else:
        break
x = int (x)
c = input("Введите c: \n")
y = input("Введите y: \n")
f = (c - (10 ** sin(c))) + (cos(c - y))
print ('f(f)=' , f)

#коммит