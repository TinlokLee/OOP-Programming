'''
    使用场景：
    设计类的继承关系时，MIxin给一个类增加多个功能
    通过多重继承，来组合多个Mixinl的功能
    在TCPServer和UDPServer网络服务时，同时服务多个用户，
    就必须使用多进程或多线程模型（ForkingMixin,ThreadingMixin）
'''
# 多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixin):
    pass

# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingServer):
    pass

# 协程模式
class MyTCPServer(TCPServer, CoroutineMixin):
    pass


'''在设计时，不需要复杂庞大的继承链，只需选择组合不同的类的功能，快速构造所需子类'''