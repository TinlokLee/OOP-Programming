#  使用__slots__ 
'''
    限制class能添加的属性，固定分配
'''
class User(object):
    __slots__ = ('name', 'age', 'score')

a = User()
a.name = "张三"
a.age = 18
a.score = 99
print(a)