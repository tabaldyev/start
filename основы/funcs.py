# Оператор return
# возвращает значение 
# останавливает функцию

# def summa(arg1, arg2):
#     return arg1+arg2 
#     print('Hello world')

# number = summa(2,3)
# print(number)
# Запустите, посмотрите что вернет функция

# Рекурсия
# вызов самого себя
# def printNumber(arg1):
#     print(arg1)
#     printNumber(arg1 + 1)

# printNumber(1)

# Cоздайте рекурсию которая возрастает
# если аргумент четный +3
# иначе +1

# def stepen(arg1, arg2):
#     return arg1 ** arg2

# num = stepen(2,7)
# print(num)
# num2 = stepen(3,3)
# print(num2)


# рекурсия
# вызов самого себя

# def generate(n, open=0, closed=0, text=''):
#     if len(text)==n*2:
#         print(text)
#         return

#     if open<n:
#         generate(n, open+1, closed, text+'😘')
#     if closed<open:
#         generate(n, open, closed+1, text+'🥰')

# generate(2)

# аргументы args

# def printsArgs(*arg):
#     for i in arg:
#         print(i)

# printsArgs(2,3,4,54,6,8)

# Задание
# найдите сумму введенных чисел
# c помощью *args

# def printsArgs(*arg):
#     sum = 0
#     for i in arg:
#         sum+=i
#     print(sum)

# printsArgs(1,4,55,2,3)


# аргументы **Kargs 

# my_dict = { 'name':'Умар'}

# def printsArgs(**arg):
   
#    for i in arg.keys():
#         print(i, '-', arg[i])
  
    
# printsArgs(student1='Умар', student2='Элзат')


# key - value
# student1 - Умар

# Лямда функции
# cокращенные функции, примерно как тернарные операторы, то есть функции в одну строку

# def firstHelloPrint(name):
#     print(f'Hello {name}')

# firstHelloPrint('Умар')

# secondHelloPrint = lambda name: print(f'Hello {name}')

# secondHelloPrint('Умар')

# sum = lambda x,y: print(x+y)

# sum(2,2)

# Cоздайте лямда функцию которая находит степень числа
# например для stepen(2,3) => 8

# sum = lambda x,y: x**y

# num = sum(2,3)
# print(num)


# Найдите большее из двух чисел с помощью лямда
# используйте тернарные операторы

# Проверьте четное ли число с помощью лямда функций
# и выведите на экран либо 'четное' либо 'нечетное'

# C помощью лямда функций сгенерируйте четные числа от 1 до введенного аргумента и выведите на экран

# С помощью лямда сравните введенный текст с 'root'
# если правильно выведите на экран 'Вход разрешен'
# иначе 'Вход запрещен'

# Найдите большее из двух чисел с помощью лямда
# используйте тернарные операторы

# Проверьте четное ли число с помощью лямда функций
# и выведите на экран либо 'четное' либо 'нечетное'

# C помощью лямда функций сгенерируйте четные числа от 1 до введенного аргумента и выведите на экран

# С помощью лямда сравните введенный текст с 'root'
# если правильно выведите на экран 'Вход разрешен'
# иначе 'Вход запрещен'

# домашнее задание
# 'если условие верное' if (cравнивание) else 'если условие не верное