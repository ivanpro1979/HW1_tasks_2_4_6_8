# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = int(input('Введите трехзначное число: '))
# summa = 0
# if 100 <= a <= 999:
#     summa = int(a % 10 + a %100 // 10 + a // 100)
#     print (summa)
# else:
#     print('вы ввели не трехзначное число') 
#    



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int(input('Введите общее число журавликов: '))
# if s % 6 == 0:
#     part = int (s / 6)
#     print(f'Петя сделал {part} журавликов, Сережа сделал {part} журавликов, Катя сделала {4 * part} журавликов,')
# else:
#      print ('Количество журавликов не удовлетворяет условиям задачи')



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# ticket = input('Введите шестизначный номер билета, для проверки счасливый билетили нет : ')
# if len(ticket) !=6:
#     print ('Введено не шестизначное число!')
# else:
#     part1 = int(ticket) / 1000
#     part2 = int(ticket) % 1000
#     summa1 = int(part1 % 10 + (part1 %100) // 10 + part1 //100)
#     summa2 = int(part2 % 10 + (part2 %100) // 10 + part2 //100)
#     if summa1 == summa2:
#         print('Yes')
#     else:
#         print('No')    



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# a = int(input('Введите размер первой стороны шоколадки: '))
# b = int(input('Введите размер второй стороны шоколадки: '))
# c = int(input('введитесколько долек нужно отломить: '))
# if c <= a*b:
#     if c % a == 0 or c % b == 0:
#         print(a, b, c, '-> yes')
#     else:
#         print(a, b, c, "-> no")  
# else:
#     print(a, b, c, "-> no")  