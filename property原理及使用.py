#  @propety 
'''
    使用场景：
    定义数据库字段类时，对其中一些类属性做字段限制，备注：一般使用set和get方法

    把一个类的getter方法变成属性,如果还有setter方法，加@method.setter

    实现原理：
    property 内封装了 __get__ __set__, __delete__ 魔法方法
    1  访问目标类属性时，触发装饰器类的__get__方法
    2  目标类赋值时，触发装饰器类的__setter__方法

    总结： @property实际上是对get和setf等方法的重写，实现了对属性的限制
'''
class User(object):
    __slots__ = ('name', 'age', 'score')

a = User()
a.name = "张三"
a.age = 18
a.score = 99
print(a)

# 属性暴露出去，没办法检查参数，值容易被修改，解决办法？
# 可以通过set（）和get（）方法解决
# class Uesr(object):
#     def set_score(self):
#         return self.set_score

#     def get_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Score must be a integer!')
#         if value < 0 or value > 100:
#             raise ValueError('Score must between 0~100')
#         self._score = value
# b = Uesr()
# b.set_score(8)
# b.get_score()
# print(b)
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(80)
s.get_score()
print(s)



#  类，函数可改写为
'''
    1 将getter方法变为属性
    2 property本身创建score.setter，将setter方法变成属性赋值
    3 最终得到一个可控的属性操作
'''
class User(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(slef, value):
        if not isinstance(value, int):
            raise ValueError("...")
        if value < 0 or value > 100:
            raise ValueError('...')
        self._score = value

s = Student()
s.set_score(80)
s.get_score()

#  实现一个可读写和只读的用户类
class User(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, data):
        self.birth = data
    
    @property
    def age(self):
        return 2018- self._birth