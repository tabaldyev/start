# def decorator(func):
#     from datetime import datetime
#     def wrapper(*args, **kyeargs):
#         start = datetime.now ()
#         func(*args, **kyeargs)
#         end = datetime.now ()
#         print(f'Скорость в начале {start} ')
#         print(f'скорость в канце {end}')
#     return wrapper


# @decorator
# def simplebeka():
#     n = int(input())
#     a = []
#     for i in range(n + 1):
#         a.append(i)
#     a[1] = 0
#     i = 2
#     while i <= n:
#         if a[i] != 0:
#             j = i + i
#             while j <= n:
#                 a[j] = 0
#                 j = j + i
#         i += 1
#     a = set(a)
#     a.remove(0)
#     print(len(a))

# simplebeka()




    

# def decorator(func):
#     def wrapper():
#         func_result = func()
#         return f'{func_result}. Успешно выполнена наша функция'
#     return wrapper


# @decorator
# def printHello():
#     def textFormat():
#         text = f'Hello'
#         return text
#     return textFormat()


# print(printHello())


# def decorator(func):

#     import time

#     def wrapper(*args, **kyeargs):
#         start = time.time()
#         func(*args, **kyeargs)
#         end = time.time()
#         print(f'Скорость нашего алгоритма в секундах{end-start}')
#     return wrapper

# @decorator
# def printHello(arg):
#     print('hello', arg)

# printHello('Умар')


# def simpleBakti():
#     countNumber = 0
#     for i in range(2, 10000):
#         countDel = 0
#         for n in range(1, i):
#             if i % n == 0:
#                 countDel+=1
#         if countDel == 1:
#             countNumber += 1
#     return countNumber


# print(simpleBakti())

# def decorator(func):

#     import time

#     def wrapper(*args, **kyeargs):
#         start = time.time()
#         func(*args, **kyeargs)
#         end = time.time()
#         print(f'Скорость нашего алгоритма в секундах{end-start}')
#     return wrapper

# @decorator
# def simplebeka():
#     n = int(input())
#     a = []
#     for i in range(n + 1):
#         a.append(i)
#     a[1] = 0
#     i = 2
#     while i <= n:
#         if a[i] != 0:
#             j = i + i
#             while j <= n:
#                 a[j] = 0
#                 j = j + i
#         i += 1
#     a = set(a)
#     a.remove(0)
#     print(len(a))

# simplebeka()

#     a=int(input("a=")) 
#     b=int(input("b=")) 
    
#     n_prime = 0 
    
#     for i in range(a,b+1): 
#         if i>1: 
#             a=2 
#             while a*a<=i: 
#                 if i%a==0: 
#                     break 
#                 a+=1 
#             else: 
#                 n_prime+=1 
            
    
    
# simplebeka()

# Геттер, сеттер

class Test:
    def __init__(self, name,surname):
        self.__name = name
        self.__surname = surname
    @property # геттер
    def getName(self):
        if self.__name == 'beka':
            return self.__name
        else:
            return 'Имя не правильное'
    @getName.setter
    def setSurName(self):
        if self.__surname == 'tabaldyev':  
            return self.__surname  
        else:
            return 'фамилия не правильно'      
    
    @getName.setter
    def setName(self, new):
        if new!='Мат':
            self.__name = new

test1 = Test('beka','tabaldyev')

test1.setName = 'Мат'
print(test1.setName)