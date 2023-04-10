#итераторы
'''Итератор — интерфейс, предоставляющий доступ 
к элементам коллекции  и навигацию по ним'''

# class Test:
    # def __init__(self, number):
    #     self.number = number
    #     self.counter = 0
    
#     def __next__(self):
#         if self.counter < self.number:
#             self.counter+=1
#             return self.counter
#         else:
#             raise StopIteration

# test1 = Test(5)
# print(next(test1))
# print(next(test1))
# print(next(test1))
# print(next(test1))

# class Test:
#     def __iter__(self):
#         return self

#     def __init__(self, number):
#         self.number = number
#         self.counter = 0
    
#     def __next__(self):
#         if self.counter < self.number:
#             self.counter+=1
#             return '*' * self.counter
#         else:
#             raise StopIteration

# test1 = Test(5)

# for i in test1:
#     print(i)

# next() вызывает след шаг
# next() делает класс итерируемым

# задача
# создайте класс который  принимает в качествеаргумента сроку
# интерируйте строку

# class Text:
#     def __init__(self,text):
#         self.text=text
#         self.counter = 0
    
#     def __iter__(self):
#         return(self)
    
#     def __next__(self):
#         if self.counter < len(self.text):
#             r=self.counter
#             self.counter+=1
#             return self.text[r]
#         else:
#             raise StopIteration
        

# text1 = Text('HELLO')

# for i in text1:
#     print(i)


#Генераторы

# class TextIterator():
#     def iter(self):
#         return self

#     def init(self, text):
#         self.text = text
#         self.currentIndex = 0
#     def next(self):
#         if self.currentIndex < len(self.text):
#             index = self.currentIndex
#             self.currentIndex +=1
#             return self.text[index]
#         else:
#             raise StopIteration

# text = TextIterator('hello')

# for i in text:
#     print(i)

# Генераторы

# def printText(arg):
#     while arg > 1:
#         arg-=1
#         yield '*' * arg

# starts = printText(5)
# for i in starts:
#     print(i)


# def printText(arg):
#     num=0
#     while arg > 1:
#         arg-=1
#         num+=1
#         yield '*' * num

# starts = printText(8)
# for i in starts:
#     print(i)

def myRange(x,y,z):
    r=0
    while r<x:
        r2=r
        r+=1
        yield r2
num = myRange(5,4,8)
for i in range(1,5,2):
    print(i)
    
