# from django.test import TestCase
#
# # def check_permission(func):
# #     def inner(*args,**kwargs):
# #         print(args,kwargs)
# #
# #
# #         return func(*args,**kwargs)
# #     return  inner
# # # Create your tests here.
# #
# #
# # @check_permission
# # def func(*args):
# #
# #     print(args)
# #
# #
# # func(15,16)
#
# #
# # a={'a':1,'b':2}
# # for v in a.keys():
# #     if a[v]==2:
# #        del (a[v])
# # #
# # # print(a)
# d = {'a':1, 'b':0, 'c':1, 'd':0}
#
# for k,v in d.items():
#     if d[k] == 0:
#         d[k]=5
# print(d)
# # a='12324'
# # for i in a:
# #     print(123)
# # print(1234)import paramiko
#
#
#
# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在known_hosts文件上的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname="192.168.101.128", port=22, username="root", password="123456")
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('ifconfig')
# # 获取结果
# result = stdout.read().decode()
# # 获取错误提示（stdout、stderr只会输出其中一个）
# err = stderr.read()
# # 关闭连接
# ssh.close()
# print(stdin, result, err)
#
#
from django.contrib.auth.hashers import make_password,check_password
kk='123456'
v=make_password(kk,None)
print(v)