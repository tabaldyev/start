




# num = int(input('введите число-'))
# if   0  <  num:
#     print('больше')
# else:
#     print('меньше')



# student = {'name': 'Ivan', 'age': 12} 

# print(student['name'])

# list=[i for i in range(1,101)]
# print(list)


# number = [i for i in range (200) if i%2==0]

# print(number)   

from browser import document, html,timer
import random

# Construction de la calculatrice
calc = html.TABLE(id='con')
lines = ['камень','ножница','бумага']

calc <= (html.DIV('DISPLAY',id='div'))

calc <= (html.DIV(html.TD(line,id='result') for line in lines))

document <= calc

result = document["result"] # direct acces to an element by its id
div = document["div"]

def action(event):
    element = event.target
    value = element.text
    robot = random.choice(lines)
    if value==robot:
        div.text='Ничея'
    elif value in "камень":
        if robot == 'бумага':
            div.text = 'Вы проиграли'
        elif robot == 'ножница':
            div.text = "Вы выиграли"
    elif value == "ножница":
        if robot == 'камень':
            div.text = 'Вы проиграли'
        elif robot == 'бумага':
            div.text = "Вы выиграли"
    elif value == "бумага":
        if robot == 'ножница':
            div.text = 'Вы проиграли'
        elif robot == 'камень':
            div.text = "Вы выиграли"

def timering(ev):
    for i in range(10):
        div.text='-'*i
    timer.set_timeout(action, 1000,ev)
    
# Associate function action() to the event "click" on all buttons
for button in document.select("td"):
    button.bind("click", timering)

# movies1 = 'Человек паук' 
# movies2 = 'Первый мститель' 
# movies3 = 'Железный человек' 
# movies4 = 'Бумер' 
# movies5 = 'Вышка' 
 
# movie = input('Введите название фильма: ') 
 
# if movie == movies1: 
#     print('Фильм который вы искали найдень ', movies1) 
# elif movie == movies2: 
#     print('Фильм который вы искали найдень ', movies2) 
# elif movie == movies3: 
#     print('Фильм который вы искали найдень ', movies3) 
# elif movie == movies4: 
#     print('Фильм который вы искали найдень ', movies4) 
# elif movie == movies5: 
#     print('Фильм который вы искали найдень ', movies5) 
# else: 
#     print('Фильм по данным ', movie, 'не найден')

# users = {'admin', 'root', 'Azis', 'Sherdos'}
# passwords = []
# while True:
#     cont = input("Что вы хотите сделать. Если зарегитрироваться нажмите на 1, если хотите войти нажмите на 2")
#     if cont == '1':
#         username = input('Введите свое имя: ')
#         password = input('Введите пароль')
#         config_password = input('Подвердите пароль')
#         if password == config_password:
#             if username in users:
#                 print('Такой пользователь уже существует')
#             else:
#                 users.add(username)
#                 passwords.append(password)
#                 print('Вы успешно зарегистрировались')
#         else:
#             print('Пароли не совпадають')
#     elif cont == '2':
#         username = input('Введите свое имя: ')
#         password = input('Введите пароль')
#         if username in users and password in passwords:
#             print('Вы успешно зашли свой аккаунт')
#         else:
#             print('Вы не зарегистрированы')
#     else:
#         print('Вы неправильно указали функцанал')