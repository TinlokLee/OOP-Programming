'''
    动态语言和静态语言的最大不同：
    函数和类的定义，不是编译时定义的，而是运行时动态创建
    创建类
    type() 和 metaclass 比较难理解，基本不用ORM框架重构时会用到
    要编写一个ORM框架，所有类都只能动态定义，只有使用者根据表结构
    定义出对应的类

'''
class User(object):
    def user(self, name='world'):
        print('User, %s' % name)
# from user import User
a = User()
a.user()
print(type(User))
print(type(a))


# type()函数即可返回一个对象的类型，又可创建出新的类型
def foo(self, name='word'):
    '''使用type创建class Hello()类 '''
    print('Hello, %s' % name)

Func = type('Func', (object,), dict(hello=foo))
f = Func()
print(f.hello)
# type（）三个参数：函数名，继承父类的集合，class的方法名与函数绑定



#  Metaclass创建类：控制类的创建行为，先metaclass再定义类，再创建实例
class ListMetaclass(type):
    ''' 自定义Mylist类增加add方法 '''
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
        # __new__()方法接受的参数：当前创建类对象，类名，类继承的父类集合，类方法结合
    
class MyList(list, metaclass=ListMetaclass):
    pass

# 测试是否可以调用add()方法
L = MyList()
L.add(1)
print(L)


'''
    编写一个ORM框架
    Object Relational Mapping 数据库的一行映射为一个对象，
                         一个字段为一列，一个类对应一个表
    1  编写底层模块，首先写调用接口，比如ORM框架
       定义一个User类来操作对应数据表User

'''
class User(Model):
    '''定义类的属性到列的映射'''
    id = InterField('id')
    name = StringField('username')
    email = StringField('email')
    passwd = StringField('passwd')

# 创建一个实例
u = User(id=123, name='Lee', email='666@163.com', passwd='passwd')
# 保存到数据库
u.save()

# 1 按上面接口，定义ORM，首先定义Field类，保存数据库表字段名，类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


 # 2 在Field类基础上，进一步定义各种类型FIeld
class StringField(Field):
    ''' 重写父类方法 '''
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name, 'bigint')


# 3 编写最复杂的ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Lee":
            return type.__new__(cls, name, bases, attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping:%s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name         # 假设表名和类名一样
        return type.__new__(cls, name, bases, attrs)


# 4 编写基类Model：初始化、访问、修改、保存权限
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' %(self.__table__, ','.join(fields), ','.join(params))
        print('SQL : %s' % sql)
        print('ARGS : %s' % str(args))
        
u = User(id=123, name='Lee', email='666@123.com', passwd='123456')
u.save()  


# 总结： metaclass是Python非常具有魔术性的对象，可改变类创建时行为，慎用！