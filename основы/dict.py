# словари
#  ключ-значение, key-value
# усписка позиция значение
# my_dict = {'name':'Бекжаннат', 'age':15}
# my_list= ['Бекжаннат',15]
# print (my_list[0])
# print (my_dict['name'])

# my_list=[]

# while True:
#     oper = input('add; Break;')
#     if oper== 'Break':
#         print(my_list)
#         break #выход из цикла
#     elif oper=='add':  
#         name,age = map(str, input ().split())
#         my_dict={'name':name, 'age':age}#создание словаря
#         my_list.append(my_dict) #добавление в список
#     else:
#         print('неверный оператор')

# изменения
# my_dict ={'name':'Бекжаннат', 'age':19}

# my_dict= [name] ='жакшылык'
# print(my_dict)

# # удаление
# deletedValue=my_dict.pop('name')
# print(my_dict)
# print('удаленное значение', deletedValue)

# settings= {'model':'mi','cores':8,'camera':'48mx' }
# for i in settings.values():
#     print(i)

# values() возвращает в список значение
# kays() возвращает в список значение

# Поставьте ограничение на возраст
# 18> если возраст меньше 18 то выведите на экран 'ваш возраст не подходит'

# my_list = []
# while True:
#     oper = input('Add; Break; ')
#     if oper=='Break':
#         print(my_list)
#         break # выход из цикла
#     elif oper=='Add':
#         name, age = map(str, input().split())
#         if int(age)<18:
#             print('Ваш возраст не подходит')
#         elif len(name)<5:
#             print('формат имени не правельный')

#         else:
#             my_dict = {'name':name, 'age': age} # создание словаря
#             my_list.append(my_dict)# добавление в список
#     else:
#         print('Неверный оператор')


# если длина имени меньше 5 то выведите на экран 'формаь имени не правильный


# тернарные операторы

# text = input()
# # if text=='Hello':
# #     print('Hi')
# # else:
# #     print('Good bye')

# # print('Hi' if text=='Hello' else 'Good bye')
# print(('Good bye', 'Hi')[text=='Hello'])

# number = int(input('Number: '))
# print(("Четное" if number % 2 ==0 else 'Нечетное'))

# спросите два числа и выведите наибольшую из них

# num = int(input())
# num2= int (input())

# print('больше'if num<num2  else 'меньше')



# number = int (input()) 
# f1 = 0
# f2 = 1
# for i in range(number):
#     fNext = f1+f2
#     f1 = f2
#     f2 = fNext
#     print(f2)

# number = int(input())
# for i in range(1, number//2 + 1):  
#     if number % i == 0:
#         print(i)

# number = int(input())
# for o in range(1, number):
#     sum = 0
#     for i in range(1, o//2 + 1):  
#         if o % i == 0:
#             sum += i
#     else:
#         if o == sum:
#             print(o)


