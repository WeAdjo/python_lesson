#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1,6):
  print(i, 0)
'''
#Задача 2
#Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
sum = 0
for i in range(10):
    answer = int(input('Напишите любое число: '))
    if answer == 5:
        sum += 1

print('Количество введеных пользователем цифр 5 - ', sum)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0
for i in range(1, 101):
    sum += i
    print(sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
n = 1
for i in range(1,11):
    n *= i

print(n)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
integer_number = 4512
# print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = 12345
n = 0
for i in str(integer_number):
    n += int(i)
print(n)
'''
Задача 7
Найти произведение цифр числа.
'''
n = 1
for i in str(integer_number):
    n *= int(i)
print(n)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 4836753
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''
Задача 9
Найти максимальную цифру в числе
'''
inter_number = 8623910
maximum = 0
# print(max(str(inter_number)))
while inter_number != 0:
    if inter_number % 10 > maximum:
        maximum = inter_number % 10
    inter_number //= 10
print(maximum)
'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 67994569365
temp = 0
while integer_number>0:
    if integer_number%10 == 5:
        temp += 1
    integer_number = integer_number//10
print(temp)