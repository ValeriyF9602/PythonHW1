# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

#
#   385916 -> yes
#   123456 -> no


number = int(input('Введите шестизначное число: '))

n1 = number // 100000 % 10
n2 = number // 10000 % 10
n3 = number // 1000 % 10
n4 = number // 100 % 10
n5 = number // 10 % 10
n6 = number % 10

if number > 99999 and number < 1000000 and n1 + n2 + n3 == n4 + n5 + n6:
    print('У вас счастливый билет!')
else:
    print('Ваш билет не является счастливым')