# Асинхронность

# Синхронный код
# print(1)
# print(2)


# def test1():
#     print('Начало первой  вункции')
#     print('Конец первой функции')
 
# def test2(): 
#     print('Начало второй вункции')
#     print('Конец вротой функции')

# def runFunc():
#     test1()
#     test2()

# runFunc()




# import asyncio
# import time

# async def test1():
#     print('Начало первой функции')
#     await asyncio.sleep(4)
#     print('Конец первой функции')

# async def test2():
#     print('Начало второй функции')
#     await asyncio.sleep(1)
#     print('Конец второй функции')

# async def runFunc():
#     task1 = asyncio.create_task(test1())
#     task2 = asyncio.create_task(test2())

#     await task1
#     await task2
    

# asyncio.run(runFunc())


# import asyncio
# import time


# async def num1():
#     print('Начало первой функции')
#     await asyncio.sleep(2)
#     for i in range (200):
#         if i % 2==0:
#             print(i,'G') 
#         await asyncio.sleep(0.1)
#     print('Конец первой функции')
# async def num2():
#     print('Начало второй функции')
#     await asyncio.sleep(2)
#     for i in range (100):
#         if i % 2==0:
#             print(i,'hy') 
#         await asyncio.sleep(0.1)
#     print('Конец второй функции')


# async def runFunc():
#     task1 = asyncio.create_task(num1())   
#     task2 = asyncio.create_task(num2())

#     await task1
#     await task2

# asyncio.run(runFunc())


# import asyncio
# import time


# async def test1():
#     print('---- Начало первой функции ----')
#     for i in range(2,200,2):
#         print(i,'первая функция')
#         await asyncio.sleep(0.01)
#     print('\033[31m','---- Конец первой функции ----', '\033[0m', sep='')

# async def test2():
#     print('---- Начало второй функции ----')
#     for i in range(2,100,2):
#         print('\033[31m', f'{i} вторая функция', '\033[0m', sep='')
#         await asyncio.sleep(0.01)
#     print('\033[31m','---- Конец второй функции ----', '\033[0m', sep='')

# async def runFunc():
#     task1 = asyncio.create_task(test1())
#     task2 = asyncio.create_task(test2())

#     await task1
#     await task2
    

# asyncio.run(runFunc())


# def test1Sync():
#     print('---- Начало первой функции ----')
#     for i in range(2,200,2):
#         print(i,'первая функция')
#     print('\033[31m','---- Конец первой функции ----', '\033[0m', sep='')

# def test2Sync():
#     print('---- Начало второй функции ----')
#     for i in range(2,100,2):
#         print('\033[31m', f'{i} вторая функция', '\033[0m', sep='')
#     print('\033[31m','---- Конец второй функции ----', '\033[0m', sep='')

# def runSyncCode():
#     test1Sync()
#     test2Sync()

# runSyncCode()


