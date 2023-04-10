# Наследование

# class test:  # родительский класс
#     name = 'умар'

# class   SomeClass(test): # дочерний класс
#     surname = ''
    
# print (test.name)
# print (SomeClass.name)



# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print('имя польз - ',self.name,', возраст - ', self.age)
    
# class Builder(User):
#     def howWork(self):
#         print('Строит')


# user1 = User('Шердос', 20)
# user2 = User('Азиз', 13)
# builder1 = Builder('Умар', 35)
# builder2 = Builder('Сергей', 34)
# builder1.info()
# builder1.howWork()

# задание 

# class Animal:
#     def __init__(self,name):
#         self.name=name

# class Dog(Animal):
#     def speak(self):
#         print ('Woof')

# class Cat(Animal):
#     def speak(self):
#         print ('Meow')

# class Cow(Animal):
#     def speak(self):
#         print ('Moo')

# dog = Dog('Тузик')
# print(dog.name)
# dog.speak()

# cat = Cat('Матроскин')
# print(cat.name)
# cat.speak()

# cow = Cow('Фердинант')
# print(cow.name)
# cow.speak()




# Одиночное и множественное наследование

# class Progmer:
#     def createProject(self):
#         print('Создать проекты')
# class Mentor:
#     def teaching(self):
#         print('Обучает')

# class User(Progmer, Mentor):
#     def __init__(self, name):
#         self.name = name

# user1 = User('Шердос')
# user1.createProject()
# user1.teaching()


# class engene:
#     def __init__(self,power,volume):
#        self.power= power
#        self.volume=volume
# class kuzov:
#     def __init__(self,color,view):
#        self.color=color
#        self.view=view
# class brand:
#     def __init__(self,country,marc) :
#         self.country=country
#         self.marc=marc

# class User(engene,kuzov,brand):
#     def moving(self):
#         self.info
#         print('делает машины')


# user1 = User()










