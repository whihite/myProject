from math import sin, cos
while True:
    x = (input("Введите x:\n "))
    if not x.isdigit():
        print ("Вы ввели букву, а надо цифру: ")
    else:
        break
x = int (x)

f = (x - (10 * sin(x))) + abs((x * 4) - (x * 5))
print ('f(x)=', f)



