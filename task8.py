# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
#
#   3 2 4 -> yes
#   3 2 1 -> no


n = int(input('Долек в шоколадке по вертикали: '))
m = int(input('Долек в шоколадке по горизонтали: '))
k = int(input('Сколько долек вы хотите получить одним разолом: '))

if k == m * n:
    print('Не нужно разламывать')
elif k < n * m and k % n == 0 or k % m == 0:
    print('Да')
else:
    print('Нет')