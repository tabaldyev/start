# ООП
# обьекто-ориентированное програмирование

# class test:
#     pass #опетарор пустышка

# class test:
#     name = 'умар' # переменные 

#     def printhello():# функции
#         print('hello word')

#     class sometext: # классы
#         pass
# print(test.name)
# test.printhello()

# принципы ООП
# наследование
# инкапсуляция
# полиморфизм
# абстракция



# инкапсуляция
# защита, сокрытие

# class  Calc:
#    __pi  = 3.1415
    
#    def AreaCircle(radius):
#         return radius * 2 * Calc.__pi
   
   
# print(Calc.AreaCircle(5)) 


# class  Calc:
#     __pi  = 3.1415 #защита переменной
    
#     def __AreaCircle(radius):
#         return radius * 2 * Calc.__pi
   
# print(Calc.__pi)
# print(Calc.__AreaCircle(5)) 

# class test:
#     name = 'beka'
#     __surname = 'tabaldyev'

    
# print(test.name)
# print(test.__surname)

# class User:
#     name = 'Умар' # статистическое
#     def __init__(self):
#         # динамическое
#         self.surname = 'Умарович'

# print(User.name)
# User.name = 'Саша'
# user1 = User()
# user2 = User()
# user1.surname = 'Васильев'
# print(user1.surname)
# print(user2.surname)
# print(user1.name)
# print(user2.name)

# статистическая переменная работает по принципу 'один для все'
# динамическое переменная 'для каждого свой'


# class User:

#     def __init__(self,name,addres,age):
#         self.name = name
#         self.addres = addres
#         self.age  = age
#     def info(self):0
#         print(f'{self.name},{self.addres},{self.age}')

# user1=User('beka','osh',20)
# user2=User('aziz','osh',19)
# user1.info()

# user2=User()
# user3=User()
# user1.name ='beka'
# user1.addres = 'osh'
# user1.age=20
# user2.name ='Aziz'
# user2.addres = 'osh'
# user2.age=19
# user3.name ='Alina'
# user3.addres = 'osh'
# user3.age=16

# print(user1.name)
# print(user1.addres)
# print(user1.age)
# print(user2.name)
# print(user2.addres)
# print(user2.age)
# print(user3.name)
# print(user3.addres)
# print(user3.age)

# print(f'{user1.name},{user1.addres},{user1.age}')
# print(f'{user2.name},{user2.addres},{user2.age}')
# print(f'{user3.name},{user3.addres},{user3.age}')



