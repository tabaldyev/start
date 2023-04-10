# text = 'hello'
# print(type(str))

# class X():
#     a='Food'
#     b=12

# o1 = type('X', (object,), dict(a='Foo', b=12))
# print(type(o1))
# text=X()
# print(type(text))

# o1 = type ('cat', (object,), dict (a= '20kg', ))
# text = o1
# print (text)


# class HelloMeta(type):
#     def hello(cls):
#         print('Hello', type(cls()))
#     def __call__(self, *args):
#         cls = type.__call__(self,*args)

#         setattr(cls, 'hello', self.hello)
#         return cls

# class TryHello(object, metaclass=HelloMeta):
#     def greet(self):
#         self.hello()
# class Wold(object, metaclass=HelloMeta):
#     def test(self):
#         self.hello()
# greeter = TryHello()
# wold = Wold()
# wold.test()

# class MetaAnimal(type):
#     def info(cls):
#         print(cls.name)

#     def __call__(self, *args, **kwds):
#         cls=type.__call__(self,*args, **kwds)

#         setattr(cls,'info',self.info)
#         return cls
    
# class Dog(object,metaclass=MetaAnimal):
#     name = 'Sharik'

# dog1=Dog()
# dog1.info()

