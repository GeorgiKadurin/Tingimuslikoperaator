﻿from math import*
from random import*



#5 Найти сумму и произведение цифр, введенного целого числа. Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).

print("Sisesta number => ")
n=int(input())
a=0
b=1
while n>0:
    c=n%10
    a=a+c
    b=b*c
    n=n//10
    print("Summa => ",a)
    print("korrutis => ", b)
    print()












#4






#3 В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

num=randint(0,100)
n=1
while n<10:
    h=int(input("juhuslik täisarv kuni 100 => "))
    if h<num:
        print("Rohkem")
    elif h>num:
        print("Väiksem")
    elif h==num:
        print("Arvasite ära ")
        break
    n+=1
print("See on number => " + str(num))
print
print()







#2 Посчитать сумму числового ряда от 0 до L (например, 14) включительно. Например, 0+1+2+3+…+14;







 





 #1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зайцев. Mежду двумя соседними зайцами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего зайца.
#
#   (\_/)
#   (o o)
#   / | \*

n=randint(1,9)
for i in range(n):

    print("    (\_/)  ")
    print("    (o o)  ")
    print("    / | \* ")
    print()
    