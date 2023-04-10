# Полиморфизм
# print(1+2)
# print('1'+'2')
# len()
# print(len('hello world'))
# print(len([1,2,3,4,5]))

# class test:
#     def  print(self):
#         print('hello world')
# class SomeClass(test):
#      def  print(self): #переобьявили
#         super().print()#супер эта метод указывающий на родителя
#         print('hello python')
# someClass = SomeClass()
# someClass.print()


# class Calc:
#     def inc(self, arg):
#         return arg + 1
#     def square(self, arg):
#         return arg*2
# class DoubleCalc(Calc):
#     def square(self, arg):
#         return super().square(arg)+arg
    
# q=DoubleCalc()
# print(q.square(5))


# class User:
#     def init(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def getInfo(self):
#         print(f"""
#         имя пользователя - {self.name}
#         фамилия пользователя - {self.surname}
#         возраст пользователя - {self.age}
#         """)


# class Student(User):
#     def init(self, name, surname, age, address ):
#         super().init(name, surname, age)
#         self.address = address
#         self.isHunged = True
        
#     def getInfo(self):
#         return super().getInfo()+(f'''
#         адресс пользователя {self.address} 
#         желудок студента {self.isHunged}''')
      

# переобьявите функцию getInfo который мы унаследовали от класса User
# используйте super
# пусть getInfo выводит всю информацию, например адресс и голодныйЛиОн(переменная)

class University:
    def __init__(self,university_name):
        self.name=university_name
        self.departaments = {}
    def add_departaments (self,fakultet_name):
        self.departaments[fakultet_name] = []
    def add_students (self, fakultet_name, student):
        lis = self.departaments[fakultet_name]
        lis.append(student.firstname)
        return self.departaments

class Students:
    def __init__(self,firstname,lastname ):
      self.firstname = firstname
      self.lastname = lastname 

university = University('osh')
students=Students('sherdos','japarov')
students2=Students('aziz','japarov')
university.add_departaments('oshmy')
print(university.add_students('oshmy',students))
print(university.add_students('oshmy',students2))


    