'''
    class中特殊用途的函数，实现自定义类的几种方法
    1  __str__()
    2  __getitem__()
    3  __getattr__()
    4  __call__()

'''
class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'User object (name : %s)' % self.name
 
# print(User('Lee'))
a = User('Lee')
print(a)

# __repr__() 调试服务，返回程序开发者看到的字符串

class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'User object (name : %s)' % self.name
    __repr__ = __str__
print(User('li'))


''' 
    __iter__() 
    用于for循环，实现__iter__方法，调用__next__取下一个值
    直到StopIterration
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.b + self.a
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

#  像list一样，按下标取元素，使用__getitem__()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 0, 1
        for x in range(n):
            a, b = b, a+b
        return a
f = Fib()
print(f[8])
# 使用切片取指定范围元素
a = list(range(100))[5:10]
print(a)
print('--------------------------------------')


''' Fib 可改写为切片取值 '''
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 0, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f[:10:5])
#  没有对step和负数做处理！！鸭子类型的实例
#  自定义的类，和Python自带list，tuple, dict一样

''' 
    动态返回一个属性, __getattr__()方法
    修改： AttributeError

    应用场景：
    针对完全动态的情况作调用，比如：
    REST API（github,sina,weibo,douban等网站）
    如果要写SDK，给每个API都写一个URL累死，API改，SDK也得改
    利用完全动态的__getattr__，实现链式调用

    概念：
    SDK：软件开发工具包（辅助开发某一软件的相关文档，范例，工具的集合）
    API：操作系统留给程序调用的接口
    DLL：动态链接库

'''
class User:
    def __init__(self):
        self.name = 'Lee'

    def __getattr__(self, attr):
        if attr == 'age':
            #return 18
            return lambda: 18

a = User()
print(a.name, a.age)
# 注意：没有找到属性，才会调用__getattr__


class Chain(object):
    '''链式调用 '''
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
# http://api.server/user/friends
# GEt /users/:user/repos  GitHub
# 调用 Chain().users('Lee').repos
print(Chain().status.user.timeline.list)


# 调用实例的方法instance.method()， 实例本身调用__call__()
class User:
    ''' 实例调用方法 '''
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)
a = User('Lee')
print(a())  

'''__call__()对象即函数，函数即对象
    通过callable()函数，判断一个对象是否是 ’可调用‘ 对象
'''     



