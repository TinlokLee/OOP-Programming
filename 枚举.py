'''
    枚举类使用场景：
    定义常量时，如月份JAN = 1

    Enum作用
    可把一组相关常量定义在一个class中，且class不可变
    成员可以直接做比较

'''
from enum import Enum, unique

Month = Enum('Month', ('Jan','Feb','Mar','Apr','May',
            'Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# 直接使用Month.Jan来引用一个常量，或枚举所有成员
# for name, member in Month.__members__.items():
#     print(name, '=Y', member, ',', member.value)

@unique
# @unique装饰器检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)

for name, member in Weekday.__members__.items():
    print(name, '=>>>', member)


'''
    把User的Gender属性改为枚举类，避免使用字符串
'''
from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class User(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试
aa = User('aa', Gender.Male)
if aa.gender == Gender.Male:
    print("测试通过")
else:
    print('测试失败')

